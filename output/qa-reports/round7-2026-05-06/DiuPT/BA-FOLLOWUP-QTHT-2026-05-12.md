# Phân loại follow-up BA — Module Quản trị hệ thống

**Nguồn:** [`BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md`](BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md)
**File tổng:** [`BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md`](BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md)
**Ngày:** 2026-05-12
**Module:** Quản trị hệ thống (FR-VIII + NFR SEC + i18n cross-module)
**Tổng items:** 8 QTHT items + 1 cross-module (#30 i18n)

**Phân loại:**
- **Nhóm A** — Cần BA quyết option (round 2): 1 item
- **Nhóm B** — Cần update SRS v3.6: 3 items
- **Nhóm C** — Dev/QA implement trực tiếp: 5 items (gồm #30 cross-module i18n)

---

## 📋 NHÓM A — Cần BA quyết option (1 item)

### A1. #27 — Endpoint read VAI_TRO cho non-QTHT

> "SRS FR-VIII-14 precondition là 'vai trò QTHT'; FR-VIII-15 form tạo tài khoản cũng chỉ QTHT. Không có căn cứ cho người không phải QTHT đọc danh sách vai trò, trừ các trường hợp đặc thù khác đã được mở rõ trong SRS."

**BA chốt:** Giữ strict QTHT-only cho quản lý vai trò.

**Chỗ chưa rõ:**
> "**Nếu** BE cần `read_vai_tro` cho dropdown nội bộ của workflow khác, phải tạo endpoint chỉ đọc có phạm vi rõ và cấp quyền rõ trong SRS, không mở ngầm."

→ **Cần Dev báo cáo + BA confirm:**
- Trong các workflow hiện tại (vd: Phân công, Mạng lưới TVV, Quản lý DN), có cần dropdown chọn vai trò không?
- Nếu CÓ → BA bổ sung endpoint readonly `GET /vai-tro/options` (hoặc tương tự) + quyền access scope
- Nếu KHÔNG → strict QTHT-only đủ, đóng item

---

## 📋 NHÓM B — Cần update SRS bổ sung spec (3 items)

### B1. #23 — Bỏ field `mat_khau` khỏi FR-VIII-15

> "SRS FR-VIII-15 hiện vẫn có input `mat_khau` bắt buộc khi tạo mới và bước xử lý hash mật khẩu, đồng thời lại gửi email kích hoạt. Nếu logic đã chốt là hệ thống tạo tài khoản rồi gửi email để người dùng đặt mật khẩu lần đầu thì SRS cần dọn lại."

**BA chốt:** Bỏ `mat_khau` khỏi form tạo tài khoản nội bộ; tạo TK ở `CHO_KICH_HOAT`, gửi liên kết kích hoạt vĩnh viễn, người dùng đặt mật khẩu qua FR-VIII-26. Chỉ giữ input mật khẩu cho DN tự đăng ký ở FR-VIII-22.

**SRS bổ sung:**
- FR-VIII-15 Inputs: **BỎ field `mat_khau`** (giữ lại cho FR-VIII-22 DN tự đăng ký)
- FR-VIII-15 Processing:
  - Bỏ bước hash mật khẩu
  - Thêm bước: gửi email kích hoạt với liên kết vĩnh viễn (theo FR-VIII-26)
- Entity TAI_KHOAN: tạo mới mặc định `trang_thai = CHO_KICH_HOAT`
- Update integration FR-VIII-15 ↔ FR-VIII-26 (flow đặt mật khẩu lần đầu)

### B2. #24 — Tách `LOAI_DOANH_NGHIEP` thành 2 danh mục

> "SRS FR-VIII-07 seed `LOAI_DOANH_NGHIEP` = DN siêu nhỏ/nhỏ/vừa, trong FR-VIII-22 lại có field `quy_mo` riêng `SIEU_NHO/NHO/VUA` và `loai_doanh_nghiep_id` riêng. Tên danh mục hiện gây nhầm giữa quy mô DN và loại hình pháp lý."

**BA chốt:** Tách thành 2 danh mục:
- `QUY_MO_DN` cho siêu nhỏ/nhỏ/vừa theo NĐ39/2018
- `LOAI_HINH_PHAP_LY_DN` cho TNHH/CP/DNTN/HKD

**SRS bổ sung:**
- Thêm 2 danh mục mới vào DANH_MUC system:
  - `QUY_MO_DN`: seed `SIEU_NHO`, `NHO`, `VUA`
  - `LOAI_HINH_PHAP_LY_DN`: seed `TNHH`, `CP`, `DNTN`, `HKD`
- Entity `DOANH_NGHIEP`:
  - Đổi field `quy_mo` → FK đến `QUY_MO_DN` (thay vì enum hardcode)
  - Đổi `loai_doanh_nghiep_id` → FK đến `LOAI_HINH_PHAP_LY_DN`
- Update FR-VIII-07 seed danh mục
- Update FR-VIII-22 form đăng ký DN với 2 dropdown riêng
- Migration: chuyển data cũ sang 2 danh mục mới

### B3. #25 — NFR SEC-06 thêm yêu cầu ký tự đặc biệt

> "Các FR chính hiện yêu cầu ký tự đặc biệt: FR-VIII-15, FR-VIII-22, FR-VIII-26 đều ghi mật khẩu ít nhất 8 ký tự, gồm chữ hoa + chữ thường + số + ký tự đặc biệt. Tuy nhiên NFR SEC-06 trong master vẫn ghi thiếu ký tự đặc biệt."

**BA chốt:** Quy tắc chuẩn: `minLength >= 8`, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, **1 ký tự đặc biệt**. Cập nhật SEC-06 cho khớp.

**SRS bổ sung:**
- NFR SEC-06 update password policy:
  - Trước: `8 ký tự, chữ hoa + thường + số`
  - Sau: `8 ký tự, chữ hoa + thường + số + ký tự đặc biệt`
- Đồng nhất với FR-VIII-15, FR-VIII-22, FR-VIII-26
- Regex/validation rule cụ thể:
  ```
  ^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[A-Za-z\d!@#$%^&*(),.?":{}|<>]{8,}$
  ```
- BE password validator update
- FE password strength meter update

---

## 📋 NHÓM C — Dev/QA implement trực tiếp (5 items)

### C1. #22 — UI text "24 giờ" sai

> "SRS FR-VIII-22 và FR-VIII-26 chốt: liên kết kích hoạt lần đầu là **vĩnh viễn, dùng 1 lần**; liên kết đặt lại mật khẩu cho tài khoản đang `HOAT_DONG` là **30 phút**. Thông báo UI '24 giờ' sai với SRS."

- **Action:** FE fix UI text label (1-line change). Đổi từ "Link có hiệu lực 24 giờ" → "Link kích hoạt có hiệu lực vĩnh viễn" (cho kích hoạt lần đầu) hoặc "Link đặt lại mật khẩu có hiệu lực 30 phút" (cho reset password).

### C2. #26 — Bỏ tab "Phiên đăng nhập" khỏi Profile

> "SRS không mô tả màn hình/tab 'Phiên đăng nhập' trong profile. Chỉ có đăng xuất, hết phiên và giới hạn số phiên đồng thời ở NFR/BR."

**BA chốt:** **Bỏ tab "Phiên đăng nhập" khỏi Profile**. Dev ẩn/xóa UI này; QA không kiểm như tính năng thuộc phạm vi phát hành.

- **Action:**
  - FE remove tab "Phiên đăng nhập" khỏi Profile UI
  - QA descope test cases liên quan tab này
  - Note: chức năng giới hạn số phiên đồng thời vẫn áp dụng ở backend (NFR), chỉ bỏ UI hiển thị danh sách phiên

### C3. #28 — Mã lỗi VAI_TRO + PWD

> "SRS QTHT dùng mã lỗi theo nghiệp vụ: `ERR-VT-01/02`, `ERR-PWD-01..06`, `ERR-TK-*`. Nếu BE dùng `ERR-VAL-VIII-*` thì không khớp SRS."

**BA chốt:** Trong phạm vi SRS v3.5 hiện tại, QA kiểm theo mã trong SRS (`ERR-VT-*`, `ERR-PWD-*`). Dev sửa BE nếu đang dùng mã khác cho cùng lỗi.

- **Action:**
  - BE align error codes: rename `ERR-VAL-VIII-*` → `ERR-VT-*` / `ERR-PWD-*` / `ERR-TK-*` theo nghiệp vụ
  - QA update test case expectations để match SRS

### C4. #29 — TVV first-login fail 401

> "Đây không phải vấn đề đặc tả nếu luồng đúng theo FR-VIII-26: token dùng 1 lần, sau khi đặt mật khẩu thành công thì TK/TVV chuyển `HOAT_DONG`, token bị hủy, người dùng đăng nhập bằng mật khẩu mới. Bị 401 sau khi form báo thành công là **lỗi triển khai hoặc lỗi môi trường kiểm thử**."

**BA chốt:** Cần tài khoản TVV/NHT mới, độc lập để kiểm thử. Kết quả đúng: đặt mật khẩu lần đầu thành công → token đã dùng → đăng nhập bằng mật khẩu mới thành công → trạng thái tài khoản và entity liên quan là `HOAT_DONG`.

- **Action:**
  - Dev debug BE token invalidation logic (kiểm tra token cleanup sau đặt password lần đầu)
  - QA chuẩn bị fixture TVV/NHT mới với password biết để re-test
  - Verify flow: form success → token hủy → login với pwd mới → trạng thái HOAT_DONG

### C5. #30 — Dấu tiếng Việt trong thông báo BE (cross-module, đặt ở QTHT)

⚠️ **Note:** Item này thuộc "P2/P3 - Vấn đề dùng chung" của file BA gốc, áp dụng **cross-module** (cả Đào tạo, Biểu mẫu, CT HTPLDN, QTHT). Đặt ở file QTHT vì là vấn đề system-level i18n.

> "Thông báo hướng người dùng trong SRS hầu hết là tiếng Việt có dấu. BE trả thông báo không dấu là nợ trải nghiệm, không nên xem là lỗi chặn phát hành nếu mã lỗi và logic đúng."

**BA chốt:** Chuẩn i18n: thông báo hiển thị cho người dùng phải có dấu tiếng Việt; log/field/code nội bộ có thể để ASCII. Dev sửa thông báo hướng người dùng, ưu tiên thông báo lỗi workflow/chính sách.

- **Action:**
  - BE i18n cleanup: convert user-facing messages từ no-dấu → có dấu
  - Ưu tiên: workflow/policy errors (Đào tạo, CT HTPLDN, Biểu mẫu)
  - Giữ ASCII cho log/code/field name nội bộ
  - QA verify: toast/message đến user phải có dấu (chỉ kiểm message hướng user, không kiểm log)

---

## 📊 Tổng kết Quản trị hệ thống

| Nhóm | Items | Count |
|:-:|---|:-:|
| **A** | #27 | 1 |
| **B** | #23, #24, #25 | 3 |
| **C** | #22, #26, #28, #29, #30 | 5 |
| **Tổng** | | **9** (8 QTHT + 1 cross-module) |

---

## 🎯 Recommend QTHT

1. **BA round 2 cho QTHT:** 1 câu hỏi (#27 endpoint VAI_TRO read-only — Dev báo cáo workflow nào cần)

2. **SRS v3.6 update cho QTHT:** 3 items
   - 1 entity change (B1: FR-VIII-15 bỏ mat_khau)
   - 1 danh mục split (B2: LOAI_DOANH_NGHIEP → QUY_MO_DN + LOAI_HINH_PHAP_LY_DN)
   - 1 NFR update (B3: SEC-06 thêm ký tự đặc biệt)

3. **Dev/QA sprint QTHT:** 5 items implement song song
   - 1 FE text fix (C1: 24h → vĩnh viễn)
   - 1 FE remove tab (C2: Phiên đăng nhập)
   - 1 BE error code align (C3: ERR-VT-* / ERR-PWD-*)
   - 1 BE debug + QA fixture (C4: TVV first-login)
   - 1 BE i18n cleanup cross-module (C5: dấu tiếng Việt)

---

## 📌 Lưu ý cross-module i18n (#30)

Item #30 áp dụng cho TẤT CẢ 4 module. Tham chiếu này được đặt ở file QTHT (system-level concern), nhưng các module khác cũng cần action:

| Module | Áp dụng #30 cho |
|---|---|
| Đào tạo | Error messages workflow duyệt CTĐT/Khóa học, thông báo gửi email kích hoạt |
| CT HTPLDN | Error messages khi trình duyệt báo cáo, tổng hợp BC |
| Biểu mẫu | Toast workflow công khai/ẩn, validation upload file (đã có dấu tốt sau BUG-BM-008/009 fix) |
| QTHT | Notifications hệ thống, error login/đặt password |

Recommend Dev BE tạo 1 task chung "BE i18n audit" để rà soát toàn bộ user-facing messages.

---

*QTHT follow-up | QA Automation 2026-05-12*
