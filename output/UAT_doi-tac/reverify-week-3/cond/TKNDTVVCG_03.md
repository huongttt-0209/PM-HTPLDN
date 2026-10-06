# Bảng đối chiếu điều kiện — TKNDTVVCG_03 (Tìm kiếm theo tên DN)

**Mã TC:** TKNDTVVCG_03 (row 291) · **Loại bug:** Tìm kiếm/Filter (phụ thuộc data) · **Verdict:** Open

Đối tác (evidence `TKNDTVVCG_03.webm`, frame t012): env `htpldn-uat.ospgroup.vn`, tài khoản CB_NV_TW, record TVCS-20260713-0001 gắn DN "Công ty cổ phần EP", nhập search "EP" → "Không có nội dung tư vấn chuyên sâu nào."

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW) | `cbnv_tw_01` (CB_NV_TW), đơn vị BTP·TW — cùng vai trò + cấp | Không |
| Entity + trạng thái (state machine) | record TVCS-20260713-0001, state "Tiếp nhận", DN "Công ty cổ phần EP" | record TVCS-SEED-0001, state "Đã duyệt", DN "Công ty TNHH Seed Publishable"; search chạy ở tab "Tất cả" (gồm mọi trạng thái). Full-text search không lọc theo state → state khác KHÔNG đổi kết quả | Không |
| Dữ liệu tiền đề (record gắn DN) | tồn tại ≥1 record gắn DN | tồn tại TVCS-SEED-0001 gắn DN "Công ty TNHH Seed Publishable"; baseline (không search) = 1 kết quả → record match được khi không có từ khóa | Không |
| Input / filter / giá trị nhập | search keyword "EP" (chuỗi con của tên DN) | search full tên DN "Công ty TNHH Seed Publishable" → 0; substring "Publishable" → 0; "TNHH" → 0; "Công ty TNHH" → 0. (Đối chứng: search mã "TVCS-SEED-0001" → 1; search nội dung "bảo mật" → 1 → endpoint hoạt động, chỉ field tên DN không được search) | Không |

**Kết luận:** 0 GAP. Search theo tên DN trả 0 kết quả dù tồn tại record khớp tên DN. Không phải min-length (full tên DN + substring dài đều 0). BE trả `{"success":true,"data":[],"meta":{"total":0}}` → BE bug (không index tên DN vào full-text search).

**Bằng chứng đối chứng số bản ghi (GATE filter/search):**
- Baseline (không search): total = **1** (DN "Công ty TNHH Seed Publishable")
- search tên DN "Công ty TNHH Seed Publishable" → total = **0** ❌
- search "Publishable" (đặc trưng tên DN) → total = **0** ❌
- search "TVCS-SEED-0001" (mã) → total = **1** ✅ (đối chứng endpoint hoạt động)
- search "bảo mật" (nội dung) → total = **1** ✅

**Phát hiện thêm (ngoài phạm vi case — search theo tiêu đề cũng hỏng):**
- search "thương mại" / "hợp đồng" (chỉ có ở tiêu đề "Tư vấn chuyên sâu về hợp đồng thương mại seed") → total = **0** ❌ → tiêu đề cũng không được search (vi phạm SRS dòng 1092).
