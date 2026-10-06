# Bảng đối chiếu điều kiện — QLNDTVVCG_36 (row 289) — Hủy record từ "Đang tư vấn"

**Case:** Hủy record đang **"Đang tư vấn"** → hệ thống **chuyển thẳng "Đã hủy"** + báo "Đã hủy yêu cầu" (đối tác cho rằng SRS yêu cầu bước "chờ duyệt hủy").
**Điểm neo SRS:** Processing Hủy yêu cầu `srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md:229` (bước 4: "Nếu DANG_TU_VAN: **yêu cầu DN đồng ý hủy + CB Phê duyệt duyệt hủy**"); SM-TVCS dòng 1512 (`DANG_TU_VAN → HUY | CB NV hủy | Guard: **DN yêu cầu hủy + CB PD duyệt** | Action: Ghi audit, TB CG + DN`). Danh sách state SM (dòng 1489–1497): 7 state, **KHÔNG có state "chờ duyệt hủy" riêng** — điều kiện duyệt hủy chỉ tồn tại dạng guard.
**Verify:** 21/07/2026, Chrome DevTools MCP. Account: CB NV `cbnv_tw_04` (CB_NV_TW, đơn vị Cục Bổ trợ tư pháp BTP·TW — cùng đơn vị record).

| Điều kiện có thể đổi kết quả | Đối tác (evidence QLNDTVVCG_36.webm) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản hủy | CB Nghiệp vụ (header BTP·TW) | `cbnv_tw_04` = CB_NV_TW, đơn vị Cục Bổ trợ tư pháp BTP·TW (cùng đơn vị record) | Không |
| Entity + trạng thái trước hủy | TVCS ở "Đang tư vấn" (DANG_TU_VAN) | TVCS-20260721-0004 ở DANG_TU_VAN (đã seed qua phân công + CG xác nhận) | Không |
| Thao tác hủy | Bấm "Hủy yêu cầu" → nhập lý do → xác nhận | Bấm [Hủy yêu cầu] → modal "Hủy nội dung tư vấn" **chỉ có 1 field "Lý do hủy"** → nhập → [Xác nhận hủy] → POST `/huy` 200, toast "Đã hủy nội dung tư vấn" | Không |
| Có bước DN đồng ý hủy + CB PD duyệt hủy? | (đối tác không thấy) | Modal KHÔNG có field/bước DN đồng ý; KHÔNG có bước CB PD duyệt hủy; hủy ngay 1 request | Không |
| State record sau hủy | Chuyển thẳng "Đã hủy" | API `trangThai=HUY` ngay sau xác nhận (không qua trạng thái trung gian) | Không |

**Kết quả verify (0 GAP):**
- Modal hủy chỉ yêu cầu **Lý do hủy** (bắt buộc). Không có bước lấy đồng ý DN, không có bước CB Phê duyệt duyệt hủy.
- Bấm [Xác nhận hủy]: **1 request** POST `/api/v1/noi-dung-tu-van-cs/{id}/huy` → **1 toast** "Đã hủy nội dung tư vấn"; API `GET` record trả `trangThai=HUY` ngay lập tức.
- Record chuyển **DANG_TU_VAN → HUY trực tiếp**, bỏ qua điều kiện guard SRS dòng 229/1512 (DN đồng ý hủy + CB PD duyệt hủy).
- Evidence: `bug-reports/tvcs/image/BD-case36-R2-dahuy.png` (record ở "Đã hủy"); `BD-case36-R2-dangtuvan.png` (trước khi hủy, DANG_TU_VAN).

**2 quan sát (ghi cả hai theo yêu cầu session):**
1. **Defect (Open):** Hệ thống cho CB NV hủy trực tiếp record DANG_TU_VAN chỉ với lý do, **bỏ qua điều kiện bắt buộc** "DN đồng ý hủy + CB Phê duyệt duyệt hủy" (SRS dòng 229 bước 4 + SM guard dòng 1512). Đây đúng phản ánh đối tác.
2. **Under-specified (BA confirm):** SM-TVCS **không có state riêng** cho bước duyệt hủy — điều kiện chỉ là guard, không có Processing sub-flow / màn hình mô tả cách DN nêu yêu cầu hủy và CB PD duyệt hủy. Cần BA chốt cơ chế duyệt hủy (ai khởi tạo, ai duyệt, có cần state trung gian không) để dev implement đúng.

**Verdict:** `Open, BA confirm` — **Open**: hủy trực tiếp vi phạm guard SRS dòng 229/1512 (tái hiện bug đối tác). **BA confirm**: cơ chế "duyệt hủy" chưa được đặc tả đầy đủ trong SM (chỉ có guard, không có state/sub-flow). Bug: `bug-reports/tvcs/Pass-bug-report-tvcs-batchD.md` (BUG-QLNDTVVCG_36); BA: `../ba-confirm/tvcs/ba-confirmation-needed-tvcs-batchD.md`.
