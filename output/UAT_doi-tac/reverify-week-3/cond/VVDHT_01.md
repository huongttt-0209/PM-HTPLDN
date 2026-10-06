# Bảng đối chiếu điều kiện — VVDHT_01 (row 200) — BC Vụ việc đang hỗ trợ (FR-IX-03)

**Đối tác phản ánh:** Đơn vị CÓ dữ liệu nhưng khi lọc theo "người hỗ trợ" (NHT phụ trách) → "Không có dữ liệu báo cáo cho kỳ...". Filter NHT trả rỗng.

**Loại bug:** Filter (phụ thuộc data + input filter) → BẮT BUỘC bảng đối chiếu, 0 GAP.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence full-res VVDHT_01.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW), header "Cán bộ NV Trung ương" | `cbnv_tw_04` (CB_NV_TW, phạm vi Toàn quốc) — cùng vai trò | Không |
| Entity + trạng thái | BC "Vụ việc đang hỗ trợ" (snapshot VV đang xử lý); đơn vị Cục Bổ trợ tư pháp có **23 VV** khi chưa lọc NHT | BC "Vụ việc đang hỗ trợ", Năm 2026, Toàn quốc → **7 VV** (Cục Bổ trợ 3, Bộ KH&ĐT 2, STP HN 1, STP AG 1). API `theoNht` có 1 NHT phụ trách 1 VV | Không |
| Dữ liệu tiền đề (VV gán NHT cụ thể) | Đơn vị có nhiều VV đang hỗ trợ; có người hỗ trợ phụ trách | ≥1 VV đang hỗ trợ gán NHT thực: "QA TVV Seed28 Active" (user-id `5432719c…`) phụ trách **1 VV** (xác nhận qua API `theoNht:[{nhtId:5432719c, soLuong:1}]`) | Không |
| Input / filter (NHT phụ trách) | Lọc lần lượt 4 NHT (Lê Gia Linh, Chuyên gia Nguyễn Văn A, Nguyễn TVV An Giang 01, Race test) → tất cả rỗng | Lọc đúng NHT đang phụ trách VV ("QA TVV Seed28 Active") → **0 VV, "Không có dữ liệu"** | Không |

**Kết luận:** 0 GAP. Đã đóng mọi tiền đề tạo được (đúng vai trò CB_NV_TW; có VV đang hỗ trợ gán NHT thực). Filter theo đúng NHT đang phụ trách 1 VV vẫn trả rỗng.

**Đo 2 phương pháp (bug candidate ≠ bug):**
- UI: chọn NHT "QA TVV Seed28 Active" → Xem báo cáo → "Không có dữ liệu báo cáo cho kỳ và đơn vị đã chọn".
- API `GET /api/v1/bao-cao/vu-viec-dang-ho-tro` (cùng kỳ Năm 2026, Toàn quốc):
  - không lọc → `tongVuViec: 7`, `theoNht:[{nhtId:"5432719c-…", ten:"", soLuong:1}]`
  - `&nhtId=98cfd963-…` (TVV-entity-id — chính là giá trị FE gửi) → `tongVuViec: 0`, `theoNht:[]`
  - `&nhtId=5432719c-…` (user-id NGUOI_DUNG) → `tongVuViec: 1`
- FE khi user chọn NHT gửi request `…&nhtId=98cfd963-…` = **id thực thể TVV** (từ `/api/v1/tu-van-viens[].id`), KHÔNG phải `taiKhoanId` (user-id) mà báo cáo dùng để khớp người xử lý → luôn 0.
→ UI khớp API, không mâu thuẫn. Bug xác thực.

**SRS:**
- `srs-fr-11-bao-cao.md:244` — Input `nht_id | identifier | N | FK → NGUOI_DUNG` (filter theo người dùng/NGUOI_DUNG).
- `srs-fr-11-bao-cao.md:247` — Công thức: đếm VV đang xử lý theo phạm vi đơn vị (người hỗ trợ là 1 chiều).
- `srs-fr-11-bao-cao.md:266` — AC: "khi lọc → chỉ hiển thị VV [thuộc điều kiện filter]".

**Verdict: Open** (hệ thống chặn luồng hợp lệ: lọc theo NHT đang phụ trách VV mà trả rỗng do sai khớp định danh NHT).
