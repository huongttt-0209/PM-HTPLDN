# TC — FR-V.II-01/04/07/10: API LGSP Side-Effect Verify (Inbound + Outbound + In-app TB)

> **UC ref**: UC68 (LGSP inbound) + UC71 (LGSP outbound) + UC74 (DN gửi đề nghị TT inbound) + UC77 (TB thẩm định in-app) | **SRS**: srs-fr-06:77-138 + 300-348 + 468-505 + 619-657
> **Roles**: CB_NV (verify side-effect UI) + TVV (verify in-app TB)
> **Mục tiêu**: Per A7 rule — KHÔNG test API thuần (JWT/mTLS/payload validation), CHỈ verify side-effect quan sát được trên UI sau khi API trigger (qua admin endpoint hoặc Postman trigger được note trong B-Seed).

## Preconditions

- Admin endpoint hoặc tool simulate LGSP push (memory `notebooklm_secondary_notebook.md` — query NotebookLM API spec)
- Login `cb_nv_tw_01` để verify HS xuất hiện
- Login `tvv_01` để verify in-app TB

## Scenarios

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-API-001 | LGSP inbound trigger (UC68) — admin push payload Mẫu 01 NĐ55 hợp lệ | 1. Trigger API push 2. Login `cb_nv_tw_01` 3. Vào /chi-tra/danh-sach 4. Refresh | HS mới xuất hiện CHO_TIEP_NHAN với mã CT-{YYYYMMDD}-{SEQ} (BR-DATA-04 auto-gen). HS lưu DOANH_NGHIEP_id, deadline SLA tính theo BR-CALC-03. AUDIT_LOG ghi nhận | BR-AUTH-09 (side-effect), BR-DATA-04, BR-CALC-03, srs-fr-06:107-110 | P0 |
| TC-CT-API-002 | LGSP outbound trigger (UC71) — sau khi UC70 kiểm tra hoàn tất | 1. Hoàn tất TC-CT-KT-002 (kết quả Đạt) 2. Verify LGSP outbound | HS có field "Đã thông báo DVC = true" (hoặc tương đương) hoặc cột status DVC. Nếu LGSP fail 3 lần → cảnh báo CB NV (in-app warning). Verify retry counter ≤ 3 | BR-RETRY-01, srs-fr-06:323-326 | P1 |
| TC-CT-API-003 (Codex FINDING-CT-03 fix) | DN gửi đề nghị TT qua DVC (UC74) — admin push payload chứng từ TT cho HS đã đánh giá | 1. Trigger API push 2. Login CB NV vào HS đó 3. Verify FILE_DINH_KEM + Verify trạng thái | Chứng từ thanh toán xuất hiện trong section File đính kèm của HS. **Trạng thái HS KHÔNG đổi do UC74** (UC74 chỉ bổ sung chứng từ — srs-fr-06:491). Mọi chuyển trạng thái sang DANG_THAM_DINH chỉ xảy ra khi hoàn tất đánh giá theo FR-V.II-05 (UC72 — srs-fr-06:390) | srs-fr-06:484-491, srs-fr-06:390 | P0 |
| TC-CT-API-004 | UC77 in-app TB sau UC76 thẩm định | 1. Hoàn tất TC-CT-TD-002 (Đạt) 2. Login `tvv_01` (TVV gắn HS) 3. Vào trang Thông báo | TB mới xuất hiện in-app: "Hồ sơ chi trả đã thẩm định: Đạt" hoặc tương đương. da_doc=false. Nội dung kèm KQ thẩm định | BR-NOTIF-01, srs-fr-06:639-642 | P1 |

## Edge bổ sung (A4 inline merge)

| TC ID | Preconditions | Steps | Expected | BR/AC ref | Severity |
|-------|---------------|-------|----------|-----------|----------|
| TC-CT-API-005 | LGSP push 2 lần với cùng `ma_ho_so_dvc` (idempotent test) | 1. Trigger lần 1 → success 2. Trigger lần 2 cùng payload | Lần 2 reject với HTTP 409 + ERR-CT-02 "Hồ sơ đã tồn tại" — backend `ma_ho_so_dvc` UNIQUE (srs-fr-06:1175). KHÔNG tạo HS trùng | ERR-CT-02, srs-fr-06:1175, EC-03 | P0 |
| TC-CT-API-006 | LGSP outbound (UC71) push timeout 3 lần | 1. Mock LGSP timeout 30s × 3 lần (BR-RETRY-01) 2. Verify cảnh báo CB NV | Sau 3 lần thất bại → log lỗi + cảnh báo CB NV in-app "Gửi kết quả kiểm tra về DVC thất bại". HS giữ trạng thái "Chưa thông báo DVC". CB NV có thể manual retry | BR-RETRY-01, srs-fr-06:325-326 | P1 |
| TC-CT-API-007 (A6 fill GAP-A5-02) | LGSP outbound (UC71) — DVC reject với HTTP 4xx (vd 403 token expired) | 1. Mock LGSP DVC reject (không retry) 2. Verify cảnh báo CB NV | ERR-CT-LGSP-02 logged. Cảnh báo CB NV in-app "DVC từ chối: token hết hạn / lỗi cấu hình LGSP" — KHÔNG retry (khác timeout). HS đánh dấu "Lỗi gửi DVC" | ERR-CT-LGSP-02, srs-fr-06:343 | P1 |

## Tổng số TC: 7 (A4 +2 edge, A6 +1 fill GAP-A5-02)

**P0: 3** | P1: 4

> **A4 audit ref:** [`08-REVIEW-edge-case-hunter.md`](08-REVIEW-edge-case-hunter.md#file-09)

> **A7 Note:** File này CHỈ verify side-effect UI. Các TC test API thuần (JWT validate, mTLS, payload schema validation, ERR-CT-AUTH-01, ERR-CT-01..03, ERR-CT-LGSP-01..02) → LOẠI A7 vì không thực hiện được qua MCP chrome-devtools (không có UI để test JWT). Nếu cần test API → forward Phase B B-Seed dùng Postman/admin endpoint.
