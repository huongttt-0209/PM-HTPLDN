# TKHSYCHTPL_06 — Bảng đối chiếu điều kiện

**Case:** Tìm kiếm không có kết quả — thông báo hiển thị (SCR-V.I-01 · FR-V.I-08 UC58 §Error Handling E1).

**Evidence đối tác:** `partner-evidence/TKHSYCHTPL_06.jpg` — **CÓ khoảnh khắc lỗi**.
Full-res: URL `htpldn-uat.ospgroup.vn/vu-viec/danh-sach?tab=TAT_CA&keyword=001&linhVucId=...&kenhTiepNhan=DVC&mucSla=BINH_THUON...`, tài khoản **"Cán bộ NV Trung ương / CB_NV_TW"**.
Bộ lọc đã áp: từ khóa **"001"** + Lĩnh vực **Thuế** + Kênh **Dịch vụ công** + Mức SLA **Bình thường** + Trạng thái **Mới tạo (+1)**.
Kết quả: bảng rỗng, các thẻ tab đều **không có số đếm**, vùng trống chỉ hiển thị icon + chữ **"Trống"**. **KHÔNG có câu "Không tìm thấy hồ sơ phù hợp"**.

**Đối tác phản ánh:** hệ thống hiển thị thông báo **"Trống"** thay vì thông báo **"Không tìm thấy hồ sơ phù hợp"**.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | **CB_NV_TW** — header ảnh "Cán bộ NV Trung ương / CB_NV_TW" | **`cbnv_tw`** — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" (đúng vai trò + cấp) | Không |
| Input / tiêu chí lọc (phải ra 0 kết quả) | Từ khóa "001" + Lĩnh vực Thuế + Kênh DVC + Mức SLA Bình thường + Trạng thái Mới tạo → **0 kết quả** | Chạy **2 truy vấn đều ra 0 kết quả**: (a) từ khóa vô nghĩa `ZZZKHONGTONTAI999`; (b) tổ hợp giống đối tác — từ khóa `001` + Kênh **Dịch vụ công** + Mức SLA **Bình thường** | Không |
| Trạng thái màn hình (danh sách rỗng do lọc, không phải do chưa có data) | Hệ thống CÓ dữ liệu (53 VV khi không lọc), rỗng là do bộ lọc | Hệ thống CÓ dữ liệu (**17 VV** khi không lọc), rỗng là do bộ lọc → đúng ngữ cảnh "tìm kiếm không ra kết quả", không phải "chưa có dữ liệu" | Không |

## Quan sát (real-data) — cbnv_tw

**Vòng 1 (bug gốc):**
```json
[{"query": "keyword=ZZZKHONGTONTAI999", "rows": 0, "empty_state_text": "Trống", "co_cau_SRS": false}]
```

**Re-test 2026-07-15 (sau dev fix) — cbnv_tw, keyword=ZZZKHONGTONTAI999 → 0 kết quả:**
```json
{"rows": 0,
 "empty_description_visible": "Không tìm thấy hồ sơ phù hợp",
 "ghi_chu": "'Trống' nay chỉ còn là alt-text ảnh minh họa; mô tả hiển thị đúng chuẩn INF-VV-TK-01"}
```
→ **PASS:** vùng rỗng do tìm kiếm 0 kết quả nay hiển thị đúng câu SRS "Không tìm thấy hồ sơ phù hợp".

Ảnh: `../../bug-reports/image/BUG-TKHSYCHTPL_06-retest-khong-tim-thay-ho-so-phu-hop.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:685` (FR-V.I-08 / UC58 §Error Handling, dòng E1): điều kiện *"Không có kết quả"* → mã **INF-VV-TK-01** → phản hồi hệ thống: **"Không tìm thấy hồ sơ phù hợp"** (severity INFO).
  (SRS lặp lại cùng thông điệp ở `:144` cho FR-V.I-01 — mã INF-VV-01, cùng câu chữ ⇒ đây là chuẩn thống nhất của module Vụ việc.)
- **Thực tế web:** vùng rỗng chỉ hiển thị icon + chữ **"Trống"** — không phải câu thông báo SRS quy định, và cũng không mang nghĩa "tìm kiếm không khớp" (người dùng dễ hiểu nhầm là hệ thống chưa có dữ liệu).
- **Đối chiếu:** SRS nêu **RÕ nội dung thông báo cụ thể** mà app không hiển thị đúng ⇒ theo §Ca biên ("SRS nêu rõ cột/vị trí/message mà app sai → Open") → **Open**, không phải BA confirm.

**Kết luận:** **Open**. Web hiển thị "Trống" thay cho thông báo bắt buộc "Không tìm thấy hồ sơ phù hợp".
