# Workflow Test Report — R7.4.A3-DN-BS (FR-V.I-NEW-02)

> **Module:** Vụ việc HTPL — DN bổ sung hồ sơ qua chuyên trang VNeID · **Round:** R13 · **Date:** 2026-05-10 03:05:00 → 03:15:00 · **Tester:** Claude Code (Opus 4.7)
> **Spec:** [`srs-update-2026-5-5/srs-fr-05-vu-viec.md`](../../../../input/srs-update-2026-5-5/srs-fr-05-vu-viec.md) §FR-V.I-NEW-02 (dòng 1288-1343) + SCR-V.I-04/05 (dòng 1846)
> **Bug:** không log — đây là test-env gap, không phải BE/FE bug.

---

## Verdict

🚫 **BLOCKED do test-env gap** — Không phải bug. Test FR-V.I-NEW-02 yêu cầu:
1. **API chuyên trang VNeID Tier 2 sandbox** (separate base URL từ `/api/v1` CMS) — chưa có URL/token.
2. **DN account VNeID Tier 2 verified** trong sandbox — chưa có DN nào.
3. **VV ở YEU_CAU_BO_SUNG state thuộc DN test** — pool 0 cho cả 2 DN test (9999999990 + 9999999991).

→ Cần dev/infra setup sandbox + dev seed data trước khi test được.

## Accounts test

| Username | Tên DN | Tier | Số VV sở hữu | VV YCBS |
|----------|--------|:----:|:------------:|:-------:|
| 9999999990 | DN Test 01 (Nguyễn Văn A) | unknown (no field) | 0 | 0 |
| 9999999991 | DN Test 02 (Trần Thị B) | unknown (no field) | 0 | 0 |

Schema `/api/v1/auth/me` từ DN context KHÔNG có field `vneidTier` / `tier` / `tierXacThuc` → BE chưa expose tier xác thực qua user info.

## Probe BE endpoints (14 candidates)

| Endpoint name | Status | Note |
|---------------|:------:|------|
| POST `/bo-sung-ho-so` | 404 | Route không tồn tại |
| POST **`/bo-sung`** (CMS) | **403 ERR-AUTH-DN-00-01** | "Role không được phép truy cập endpoint CMS này" — endpoint CMS, DN bị reject (đúng spec dòng 491 BR-AUTH-10) |
| POST `/cap-nhat-ho-so` | 404 | — |
| POST `/upload-ho-so` | 404 | — |
| POST `/submit-supplement` | 404 | — |
| POST `/supplement` | 404 | — |
| POST `/gui-bo-sung` | 404 | — |
| POST `/nop-bo-sung` | 404 | — |
| POST `/them-tai-lieu` | 404 | — |
| POST `/upload-tai-lieu` | 404 | — |
| POST `/them-ho-so` | 404 | — |
| POST `/gui-ho-so` | 404 | — |
| POST `/gui-tai-lieu` | 404 | — |
| POST `/cap-nhat-tai-lieu` | 404 | — |

**Phát hiện:** Endpoint `/bo-sung` TỒN TẠI nhưng là CMS endpoint (cho CB NV xem hồ sơ), KHÔNG phải endpoint cho DN-portal. Per spec dòng 491:
> "BR-AUTH-11: Lọc API cho DN (chuyên trang Cổng PLQG): DN KHÔNG đăng nhập CMS → không có phiên phân quyền dữ liệu. DN tương tác qua API chuyên trang."

→ **API chuyên trang VNeID Tier 2 phải ở base URL riêng** (không phải `/api/v1` CMS). Chưa có thông tin URL/path/token cho sandbox này.

## UI DN context (9999999991)

Sidebar DN chỉ có 5 button:
- Tổng quan
- Quản lý đào tạo, tập huấn
- Quản lý vụ việc hỗ trợ pháp lý
- Quản lý chi trả chi phí
- Quản lý doanh nghiệp được hỗ trợ

→ Sidebar DN trên CMS chỉ là **read-only view của VV của DN** (theo spec dòng 1846 "chỉ 2 nút DN được phép: [Bổ sung hồ sơ] + [Đánh giá]"). Quản lý vụ việc trong CMS không phải chuyên trang VNeID DN-portal.

Filter tab trong list VV DN view: "Tất cả / Chờ tiếp nhận / Đang xử lý / Chờ phê duyệt / Hoàn thành / Từ chối" — **KHÔNG có tab "Yêu cầu bổ sung"** (UI gap có thể là intent — YCBS gộp vào "Đang xử lý"). Cần BA confirm.

DN test 01 + 02 đều có 0 VV → Empty state "Không có dữ liệu" hiển thị, không thể click thử button [Bổ sung hồ sơ].

## Test scope (per todo R7.4.A3-DN-BS)

| # | Test scenario | Status | Note |
|---|--------------|:------:|------|
| 1 | DN auth VNeID Tier 2 → access chuyên trang | 🚫 BLOCKED | Sandbox chưa setup |
| 2 | DN xem VV YEU_CAU_BO_SUNG của mình | 🚫 BLOCKED | Pool 0 + sandbox |
| 3 | DN click [Bổ sung hồ sơ] → form embedded | 🚫 BLOCKED | Cần (1) + (2) |
| 4 | DN upload tài liệu + submit | 🚫 BLOCKED | Endpoint chuyên trang chưa rõ |
| 5 | State YEU_CAU_BO_SUNG → DANG_KIEM_TRA | 🚫 BLOCKED | Cần (4) |
| 6 | Notification CB NV khi DN bổ sung | 🚫 BLOCKED | Cần (5) |
| 7 | Quá hạn auto-reject (BR-EC-16) | 🚫 BLOCKED | Cần SLA bo_sung_timeout config |

## Spec FR-V.I-NEW-02 áp dụng

Section §FR-V.I-NEW-02 dòng 1288-1343:
- Pre: VU_VIEC.trang_thai = YEU_CAU_BO_SUNG
- DN auth VNeID Tier 2 (BR-AUTH-01 line 685)
- Process: upload file → lưu HO_SO_VU_VIEC → transition YCBS → DANG_KIEM_TRA
- Notification: TB CB NV
- BR-EC-16: quá hạn auto-reject

Cross-ref:
- `srs-fr-05-vu-viec.md:210` "DN truy cập PM (auth VNeID Tier 2) **When** chọn 'Gửi yêu cầu HTPL'"
- `srs-v3.5.md:685` "INT-02 VNeID (qua NDXP) — Xác thực danh tính điện tử theo mô hình 2-tier"

## Đề xuất unlock

1. **Dev/Infra:** Setup VNeID Tier 2 sandbox URL + cấp DN test account đã verify Tier 2.
2. **Dev BE:** Confirm endpoint chuyên trang DN-portal (path + auth method) cho FR-V.I-NEW-02.
3. **Dev BE:** Seed ≥1 VV ở YEU_CAU_BO_SUNG state thuộc DN test (9999999990 hoặc 9999999991) để QA test E2E.
4. **BA:** Confirm filter tab "Yêu cầu bổ sung" ẩn cố ý hay là gap UI — ảnh hưởng UC DN tìm VV cần bổ sung.
5. QA re-test R14 sau khi (1)+(2)+(3) sẵn sàng.

## Cascade impact

- **R7.4.A3-DN-BS** todo: BLOCKED toàn task — không có sandbox + data + endpoint.
- **R7.7.3** functional test: test cases liên quan YCBS → DANG_KIEM_TRA transition (FR-V.I-NEW-02 path) cũng blocked.

*2026-05-10 03:15:00 — R7.4.A3-DN-BS BLOCKED do test-env gap (sandbox VNeID T2 + DN VV YCBS data), KHÔNG log bug. Escalate dev/infra setup sandbox.*
