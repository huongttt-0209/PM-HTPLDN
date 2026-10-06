# QLHDTVVCG_23 — khóa chuẩn chấm (Giai đoạn A, flow 04)

**Dòng bảng:** 329 · **Mô tả (G):** Bỏ liên kết
**Điều kiện (H):** 1. Điều kiện hiển thị: trên mỗi dòng của bảng vụ việc liên kết (Nhóm 2)
**Bước (J):** 1. Mở Nhóm 2 (Vụ việc liên kết) của biểu mẫu chi tiết · 2. Bấm nút "Bỏ liên kết"
**Trạng thái (N):** `N/R` — phiếu chưa từng chạy ⇒ **expected đối tác = nguyên văn cột K**.

**Nguồn chuẩn:** `srs-fr-14-hop-dong-tv.md` §3 (SCR-X3-01)
**Kiểm chéo:** `srs-fr-05-vu-viec.md` §E (bảng thông báo/hộp xác nhận chung)

> 🔴 **Phiếu này có 1 vế `GAP` → CẤM Pass toàn phiếu, kết luận Cần BA** (dù C2 đo đạt).

---

## a) Bảng khóa vế

| Vế | Expected đối tác (nguyên văn ý cột K) | Neo SRS | Quan hệ | Route | Đường đo ngắn nhất + đối chứng độc lập |
|---|---|---|---|---|---|
| **C1** | "Hệ thống **hỏi xác nhận** "Bạn có chắc chắn muốn bỏ liên kết vụ việc «{mã vụ việc}»?"" | **IM LẶNG** — `:291` chỉ khai nút `[Bỏ liên kết]` trên bảng, **không** khai hộp xác nhận cũng không khai câu chữ. Bảng thông báo chung `srs-fr-05-vu-viec.md:1588`–`:1597` (đã đọc trọn) **không có** mục nào cho thao tác bỏ liên kết | **GAP** | **BA** | Chỉ đo hiện trạng: bấm nút, ghi lại có hộp xác nhận không và nguyên văn câu chữ (có chèn mã vụ việc hay không). **CẤM Pass/Reopen vế này** |
| **C2** | "Nếu xác nhận, hệ thống **bỏ dòng khỏi bảng**" | `srs-fr-14-hop-dong-tv.md:291` (nút `[Bỏ liên kết]` nằm ngay trên dòng của bảng VV liên kết — mục đích của nút) | **MATCH** | TEST | **UI:** ghi số dòng + mã vụ việc trước khi bấm → bấm Bỏ liên kết → xác nhận → dòng đó biến mất, số dòng giảm đúng 1. **Đối chứng:** đọc lại bản ghi hợp đồng qua API, danh sách vụ việc liên kết **không còn** mã đó |

---

## b) Nguyên văn dòng SRS đã trích

**`srs-fr-14-hop-dong-tv.md:291`** (dòng duy nhất khai nút `[Bỏ liên kết]` — neo của C2, và là dòng gần nhất cho `GAP` C1)
```
| 7 | content (form) | Accordion: Vụ việc liên kết | table + modal | Bảng VV liên kết: Mã VV / Tên DN / Lĩnh vực / Trạng thái / [Bỏ liên kết]. Nút [+ Liên kết VV] -> modal multi-select. N:N | click -> action | trang thêm/sửa — chỉ CB NV |
```
> Toàn bộ đặc tả nhóm X.3 **chỉ có một dòng này** nhắc tới "Bỏ liên kết". Không có bước Processing riêng, không có mã lỗi/thông báo riêng.

**`srs-fr-14-hop-dong-tv.md:118`**–**`:125`** (Processing FR-X.3-01 — **trọn bảng**, bằng chứng đặc tả không khai bước bỏ liên kết)
```
| 1 | Kiểm tra quyền. CB NV: áp phân quyền đơn vị (BR-AUTH-08). TVV/CG: chỉ trả HĐ có `tu_van_vien_id` thuộc về user đang đăng nhập; chặn mọi thao tác Create/Update/Delete | BR-AUTH-01, BR-AUTH-08 |
| 2 | Thêm mới: sinh mã tự động HDTV-{YYYYMMDD}-{SEQ} | BR-DATA-04 |
| 3 | Kiểm tra: ngày bắt đầu <= ngày kết thúc | — |
| 4 | Kiểm tra: tổng thanh toán giai đoạn <= giá trị HĐ | — |
| 5 | Tạo hoặc cập nhật bản ghi hợp đồng + mốc tiến độ + thanh toán giai đoạn | — |
| 6 | Liên kết vụ việc: tạo liên kết many-to-many | — |
| 7 | Xóa: chỉ khi KHÔNG có vụ việc liên kết, xóa mềm | BR-DATA-01 |
| 8 | Ghi nhật ký thao tác | BR-DATA-05 |
```
> Có bước **tạo** liên kết (bước 6), **không có** bước **gỡ** liên kết.

**`srs-fr-14-hop-dong-tv.md:166`**–**`:173`** (Error Handling FR-X.3-01 — **trọn bảng**, không có thông báo/xác nhận cho bỏ liên kết)
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

**`srs-fr-05-vu-viec.md:1595`**–**`:1596`** (§E — hai mục xác nhận **duy nhất** của quy ước chung, đều **cho vụ việc**, không cho bỏ liên kết)
```
| Xóa hồ sơ | Confirm modal | Tiêu đề: "Xác nhận xóa vụ việc". Nội dung: "Bạn có chắc chắn xóa vụ việc {ma_vu_viec}? Hồ sơ sẽ được lưu trong thùng rác và quản trị viên có thể khôi phục." Nút: [Xóa] / [Hủy] |
| Xóa hàng loạt | Confirm modal | "Bạn sắp xóa {N} vụ việc. Tiếp tục?" |
```
> Mẫu câu của đối tác ("Bạn có chắc chắn muốn bỏ liên kết vụ việc «{mã vụ việc}»?") **giống về văn phong** với dòng `:1595` nhưng đó là câu **xóa vụ việc**, không phải **bỏ liên kết hợp đồng ↔ vụ việc**. Không được mượn dòng này làm chuẩn chấm.

**`srs-fr-14-hop-dong-tv.md:299`** (Quy tắc tương tác — cho thấy bỏ liên kết ảnh hưởng điều kiện xóa hợp đồng)
```
- Xóa HĐ: chỉ khi KHÔNG có vụ việc liên kết (soft delete)
```

---

## c) Tiền đề tối thiểu

| Hạng mục | Yêu cầu | Suy từ dòng nào |
|---|---|---|
| **Vai trò / tác nhân** | **Cán bộ Nghiệp vụ (TW/BN/ĐP)** — bắt buộc. Cột `Tác nhân` (F) RỖNG ⇒ suy từ `:291` ("trang thêm/sửa — **chỉ CB NV**"), `:68`, `:118` (TVV/CG chặn mọi thao tác Update) | `:68`, `:118`, `:291` |
| **Tài khoản** | `cbnv_tw_03` / `Test@1234` | brief §3 |
| **Màn đo** | **Biểu mẫu thêm/sửa hợp đồng**, Nhóm 2 — `:291` chỉ khai nút `[Bỏ liên kết]` cho **trang thêm/sửa** | `:291` |
| **Dữ liệu — quyết định** | **1 hợp đồng có ≥2 vụ việc liên kết.** Cần ≥2 (không phải ≥1) để sau khi bỏ 1 dòng vẫn còn bảng mà đếm, và để phân biệt "bỏ đúng dòng đã chọn" với "xoá sạch bảng" | `:291` |
| **Ghi mốc so trước khi bấm** | Ghi **số dòng** và **mã vụ việc của dòng sắp bỏ** trước khi thao tác. Không có mốc so thì C2 không đối chứng được | `:291` |
| **Cách dựng** | Chạy `_22` trước để tạo liên kết, hoặc dùng lại hợp đồng đã dựng ở `_15`/`_09`. **Chạy `_23` SAU `_18`** — nếu bỏ hết liên kết trước thì `_18` (xóa khi có vụ việc liên kết) mất tiền đề | thứ tự chạy ở `00-TONG-HOP-QLHDTVVCG.md` |
| **Khai báo thay đổi** | Bỏ liên kết **là mutate môi trường chung** ⇒ báo cáo khai: hợp đồng nào · gỡ vụ việc nào · env nội bộ | brief §4.5 |

---

## d) Bẫy chấm oan

**Dễ Pass oan:**
- **Dòng biến khỏi bảng nhưng liên kết chưa gỡ ở máy chủ.** Giao diện có thể chỉ gỡ dòng trong bộ nhớ, chờ bấm Lưu mới ghi xuống. **Bắt buộc** đọc lại bản ghi hợp đồng qua API sau khi xác nhận. Nếu hệ thống yêu cầu bấm Lưu mới có hiệu lực, ghi rõ điều đó — cột K chỉ nói "bỏ dòng khỏi bảng", nên vế C2 vẫn có thể đạt, nhưng phải mô tả trung thực.
- **Bỏ nhầm dòng khác.** Bảng nhiều dòng, nút trên từng dòng dễ bấm lệch. Phải so **mã vụ việc** của dòng biến mất với dòng đã chọn — đây là lý do tiền đề đòi ≥2 dòng.
- **Đếm gộp thẻ bọc ngoài với thẻ con** → số dòng nhân đôi, không phát hiện được giảm 1. Đếm bằng selector dòng cụ thể.
- **Kết luận C1 "đạt" vì có hộp xác nhận đúng y câu chữ đối tác nêu.** C1 đã khóa `GAP` — **kết quả đo không đổi được quan hệ** (flow 04 luật khóa 5). Trong tóm tắt phải nói rõ "web hiện tại **đúng kỳ vọng đối tác**" để không bị đọc nhầm thành lỗi; câu hỏi BA là **bổ sung điều này vào đặc tả**, không phải chặn bàn giao.

**Dễ Fail oan:**
- **Fail C1 vì không có hộp xác nhận, hoặc câu chữ khác, hoặc không chèn mã vụ việc.** Đặc tả **không** quy định gì về hộp xác nhận cho thao tác này ⇒ không Fail, chuyển BA.
- **Fail vì mượn câu ở `srs-fr-05-vu-viec.md:1595` làm chuẩn.** Dòng đó là câu **xóa vụ việc**, không phải bỏ liên kết — mượn nhầm sẽ tạo yêu cầu mà đặc tả không hề ghi.
- **Fail vì nút "Bỏ liên kết" là biểu tượng chứ không phải chữ.** Phụ lục E §H6 (`srs-v3.5.md:6758`) bắt cột Hành động dùng **icon + tooltip** ⇒ icon là **đúng**.
- **Fail vì vụ việc vẫn tồn tại sau khi bỏ liên kết.** Bỏ liên kết chỉ gỡ quan hệ, **không** xóa vụ việc. Vụ việc còn nguyên là **đúng**.
- **Fail vì phải bấm Lưu mới có hiệu lực.** Đặc tả không khai thời điểm ghi xuống; cột K chỉ nói "bỏ dòng khỏi bảng". Ghi nhận hành vi, không Fail.
