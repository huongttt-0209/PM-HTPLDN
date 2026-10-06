# Bảng đối chiếu điều kiện — QLNDTVVCG_23 (row 287) — Phân công CG

**Case:** Đối tác chọn 1 CG + bấm "Phân công" → hệ thống báo **"Phân công thất bại"**.
**Điểm neo SRS:** Processing Phân công CG `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:154-163` (step 3: CG đang hoạt động + chuyên môn phù hợp lĩnh vực); SM TIEP_NHAN→PHAN_CONG dòng 1504 (guard "Có CG/TVV phù hợp").
**Verify:** 21/07/2026, Chrome DevTools MCP, account `cbnv_tw_04` (CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp).

| Điều kiện có thể đổi kết quả | Đối tác (evidence full-res QLNDTVVCG_23.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB Nghiệp vụ Trung ương (CB_NV_TW), header "BTP · TW" | `cbnv_tw_04` = CB_NV_TW, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp (BTP-TW) | Không |
| Entity + trạng thái | TVCS ở TIEP_NHAN, mở modal "Phân công chuyên gia" | TVCS-20260721-0003 ở TIEP_NHAN, mở modal "Phân công chuyên gia" | Không |
| CG được chọn (loại + trạng thái) | "huongcg" — modal offer (đã lọc loaiTvv=CG + lĩnh vực khớp), card Chuyên môn hiển thị "—" | qa_tvvseed28 (TVV-BTP-TW-0002) — loaiTvv=CG, HOAT_DONG, modal offer, card Chuyên môn hiển thị "—" (chuyenNganh null, giống hệt đối tác) | Không |
| Chuyên môn CG khớp lĩnh vực record | huongcg offered → khớp lĩnh vực record | qa_tvvseed28 chuyên môn Thương mại = lĩnh vực record Thương mại (linhVucIds trùng bbbbbbbb-...001c) | Không |

**Đóng GAP tiền đề (§Nguyên tắc 4):** env nip.io ban đầu 0 CG loaiTvv=CG trong đơn vị → dropdown modal rỗng ("Không có CG phù hợp với lĩnh vực này"). Đã chuyển `qa_tvvseed28` (TVV-BTP-TW-0002) loaiTvv TVV→CG qua `PATCH /api/v1/tu-van-viens/{id}` (account có role CG sẵn, đơn vị + lĩnh vực đã đúng) → CG hợp lệ xuất hiện trong modal → test đúng điều kiện đối tác.

**Kết quả verify (0 GAP):**
- Chọn qa_tvvseed28 (offered, active, chuyên môn Thương mại khớp lĩnh vực) → bấm "Phân công".
- `toast-capture.js` (observer self-check = 1): **1 request** `POST /api/v1/noi-dung-tu-van-cs/{id}/phan-cong` → **200**; **1 toast** = **"Đã phân công chuyên gia"** (KHÔNG phải "Phân công thất bại").
- Record chuyển TIEP_NHAN → **PHAN_CONG**, Chuyên gia = "QA TVV Seed28 Active", stepper bước 1 ✓ bước 2 active.
- Evidence: `bug-reports/tvcs/image/BD-case23-phancong-result.png` (state PHAN_CONG + success); `bug-reports/tvcs/image/BD-case23-modal-dropdown-search.png` (dropdown state).

**Verdict:** `Reject` — Đối tác báo lỗi cụ thể "Phân công thất bại"; verify đúng điều kiện (CG hợp lệ, đủ điều kiện SRS step 3) thì phân công **THÀNH CÔNG**, lỗi KHÔNG tái hiện. Env đối tác (htpldn-uat.ospgroup.vn) khác env verify (18.143.165.120.nip.io) → nghi lỗi build/env cũ đã fix. → Đối tác kiểm tra lại.

**Loại trừ nguyên nhân data:** card "Chuyên môn: —" (dash) xuất hiện ở CẢ đối tác lẫn mình (do field chuyenNganh null, khác linhVucText) nhưng KHÔNG gây fail — chứng minh "—" chỉ là hiển thị cosmetic, không phải nguyên nhân "Phân công thất bại".
