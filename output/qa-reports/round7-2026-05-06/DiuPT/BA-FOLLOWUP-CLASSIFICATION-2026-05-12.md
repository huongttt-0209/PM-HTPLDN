# Phân loại follow-up từ BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11

**Nguồn:** [`BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md`](BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md)
**Ngày phân loại:** 2026-05-12
**Người phân loại:** QA (Claude Code MCP)
**Mục đích:** Sau khi BA trả lời 30 items, phân loại từng item theo loại action tiếp theo:
- **Nhóm A** — Cần BA quyết option / chốt hẳn (round 2 BA confirm)
- **Nhóm B** — BA đã chốt direction, cần update SRS bổ sung spec
- **Nhóm C** — Implementation/QA align (Dev/QA action, không cần BA confirm thêm)

---

## 📋 NHÓM A — Cần BA quyết option / chốt hẳn (4 items)

**Định nghĩa:** BA đã trả lời nhưng để ngỏ option ("có thể", "trừ khi", "nếu") → cần BA round 2.

### A1. #5 — CT HTPLDN hoàn thành "0/0 đợt báo cáo"

> BA propose 2 option: (1) thêm cờ `khong_yeu_cau_bao_cao`; (2) không thêm cờ, đổi message error. Chưa chốt option nào.

- **Cần BA chọn:** Option 1 hay Option 2

### A2. #11 — Điểm vào tạo Học viên

> "CMS CB NV chỉ duyệt/quản lý... không tạo HV thay DN **trừ khi có UC bổ sung**."

- **Cần BA xác nhận:** Có UC nào cho CB NV tạo HV trực tiếp không? Nếu có thì UC nào?

### A3. #13 — Sĩ số tối đa khi DU_THAO

> "**Có thể cho phép** bỏ trống khi lưu nháp."

- **Cần BA quyết hẳn:** DU_THAO cho phép `null/0` hay luôn bắt buộc `>=1`?

### A4. #27 — Endpoint read VAI_TRO cho non-QTHT

> "Nếu BE cần `read_vai_tro` cho dropdown nội bộ, phải tạo endpoint riêng + spec rõ trong SRS."

- **Cần Dev báo cáo + BA confirm:** Workflow nào cần dropdown VAI_TRO? Nếu có → spec endpoint readonly.

---

## 📋 NHÓM B — BA chốt rồi, cần update SRS bổ sung spec (14 items)

**Định nghĩa:** BA quyết direction rõ ràng, nhưng SRS v3.5 chưa có spec chi tiết → cần SRS v3.6 hoặc patch.

### B1. #1 — Endpoint public cho chuyên trang Cổng PLQG

> "Dev cần tách endpoint public hoặc bổ sung rõ rule cho endpoint đó."

- **SRS bổ sung:** URL pattern, auth (mTLS từ Cổng PLQG), filter rule `cong_khai=true AND trạng thái publishable`. Tách rõ public API khỏi CMS API.

### B2. #4 — Đề kiểm tra: không cần duyệt + quy tắc xóa

> "Không cần phê duyệt riêng. 'Chưa sử dụng' để xóa là: chưa `DA_PHAN_PHOI` **AND** chưa có `KET_QUA_DAO_TAO.de_kiem_tra_id` liên kết."

- **SRS bổ sung:** FR-III-NEW-01/02/03 thêm BR rõ "không có workflow duyệt" + định nghĩa "chưa sử dụng" để xóa (2 điều kiện).

### B3. #7 — 3 field từ chối kết quả đào tạo

> "Bổ sung trường riêng: `ly_do_tu_choi_kq`, `thoi_gian_tu_choi_kq`, `nguoi_tu_choi_kq`."

- **SRS bổ sung:** Entity `KHOA_HOC` thêm 3 column; FR-III-18 Inputs/Outputs/Processing update; migration DB.

### B4. #10 — Tài khoản HOC_VIEN không bắt buộc

> "`taiKhoanId` của HOC_VIEN là **không bắt buộc**, HV được quản lý dưới TK DN/NHT đã đăng ký."

- **SRS bổ sung:** Entity `HOC_VIEN.tai_khoan_id` NULL allowed; FR-III-19 làm rõ "HV không có TK riêng"; BR-AUTH-USERNAME-01 confirm không có convention sinh username cho HV.

### B5. #12 — Hình thức Khóa học `KET_HOP`

> "Thêm enum `KET_HOP` cho `KHOA_HOC.hinh_thuc`. Khi `KET_HOP`, từng `LICH_HOC.hinh_thuc_buoi` bắt buộc chọn `TRUC_TUYEN`/`TRUC_TIEP`."

- **SRS bổ sung:** Update CHECK constraint `hinh_thuc IN ('TRUC_TUYEN', 'TRUC_TIEP', 'KET_HOP')`; entity `LICH_HOC` field `hinh_thuc_buoi`; FR-III-22 validation rule.

### B6. #15 — Quy tắc chống trùng lịch học

> "Bổ sung `BR-LH-CONFLICT-01` vào FR-III-22: không cho tạo/sửa buổi học trùng khoảng thời gian trong cùng Khóa học."

- **SRS bổ sung:** BR mới + error code `ERR-LH-CONFLICT-01` + Vietnamese message; defer mở rộng theo `giang_vien_id` tương lai.

### B7. #16 — 2 API inbound từ Cổng PLQG

> "BA/SRS cần bổ sung endpoint inbound riêng: (a) API tiếp nhận đăng ký đào tạo; (b) API tiếp nhận/thêm học viên."

- **SRS bổ sung:** 2 endpoint specs trong FR-16 (path, auth mTLS+JWT, request/response shape, idempotency, anti-duplicate, validation).

### B8. #17 — Transition TW `DA_DUYET_KQ → DA_TONG_HOP`

> "Thêm chuyển trạng thái riêng cho TW: `DA_DUYET_KQ -> DA_TONG_HOP` khi đợt báo cáo thuộc TW."

- **SRS bổ sung:** Update SM-DOT-BC với transition mới + guard `dot_bao_cao.don_vi.cap = 'TW'`; FR-XI-09 action "Xác nhận tổng hợp nội bộ TW".

### B9. #19 — `/start` cho phép `soLieuTongHop.fields` rỗng

> "`/start` được tạo khung báo cáo rỗng, validation tại bước trình duyệt."

- **SRS bổ sung:** FR-XI-06 làm rõ "POST /start: fields có thể rỗng"; validation chuyển sang bước `DANG_LAP_BC → CHO_DUYET_KQ` (kiểm `fields` non-empty + đủ trường bắt buộc theo mẫu 21a/21b).

### B10. #20 — Response `POST /tong-hop` đổi shape

> "Đổi response thành `dotBaoCaoIds: []`, `baoCaoTongHopId`, `soDotTongHop`."

- **SRS bổ sung:** FR-XI-09 Outputs update; `danh-sach-api.md` cập nhật response shape; BE migration backward compatibility.

### B11. #21 — Quyền NHT/BN/ĐP với BIEU_MAU

> "Phạm vi đọc: own-unit **AND** biểu mẫu cấp TW dùng chung. Không thấy ngang cấp khác."

- **SRS bổ sung:** Định nghĩa "biểu mẫu cấp TW dùng chung" (cờ `dung_chung: boolean` HAY default mọi TW BM = dùng chung); update BR-AUTH-08 cho BIEU_MAU/THU_MUC_BIEU_MAU; update FR-VII rule + permission-matrix line 534.

### B12. #23 — Bỏ field `mat_khau` khỏi FR-VIII-15

> "Bỏ `mat_khau` khỏi form tạo tài khoản nội bộ; tạo TK ở `CHO_KICH_HOAT`, gửi liên kết kích hoạt vĩnh viễn."

- **SRS bổ sung:** FR-VIII-15 Inputs bỏ `mat_khau`; Processing bỏ hash, thêm bước gửi email kích hoạt; entity TAI_KHOAN default `trang_thai=CHO_KICH_HOAT`; integration với FR-VIII-26.

### B13. #24 — Tách `LOAI_DOANH_NGHIEP` thành 2 danh mục

> "(a) `QUY_MO_DN` (SIEU_NHO/NHO/VUA per NĐ39/2018); (b) `LOAI_HINH_PHAP_LY_DN` (TNHH/CP/DNTN/HKD)."

- **SRS bổ sung:** 2 danh mục mới + seed values; entity `DOANH_NGHIEP` đổi `quy_mo` thành FK + đổi `loai_doanh_nghiep_id` semantics; update FR-VIII-07 seed + FR-VIII-22 form; migration data cũ.

### B14. #25 — NFR SEC-06 thêm ký tự đặc biệt

> "minLength >= 8, có ít nhất 1 chữ hoa, 1 chữ thường, 1 chữ số, **1 ký tự đặc biệt**. Cập nhật SEC-06 cho khớp."

- **SRS bổ sung:** Update NFR SEC-06 password policy đồng nhất với FR-VIII-15/22/26; regex/validation rule cụ thể.

---

## 📋 NHÓM C — Implementation/QA align (12 items không cần BA confirm thêm)

**Định nghĩa:** BA chốt rõ ràng dựa trên SRS v3.5 hiện có hoặc decision đơn giản → Dev/QA implement trực tiếp, **không cần update SRS hoặc BA confirm thêm**.

### C1. #2 — Lộ data KH năm xuyên đơn vị

> "Nếu API đang trả 7 bản ghi từ 3 `donViId` cho BN/ĐP thì đó là **lỗi lộ dữ liệu**, không phải điểm mơ hồ của SRS."

- **Action:** Dev fix BE bug (apply BR-AUTH-03/04/08 đúng); QA verify scope per role.

### C2. #3 — Khóa học 9 trạng thái

> "SRS v3.5 đã chốt 9 trạng thái... Nếu BE/UI hiện chỉ có khoảng 6 trạng thái thì BE/UI đang thiếu."

- **Action:** BE/UI implement đủ 9 trạng thái theo SRS; QA update test cases.

### C3. #6 — Tên trường lý do từ chối (Đào tạo)

> "Dùng trường riêng `ly_do_tu_choi/thoi_gian_tu_choi/nguoi_tu_choi`. BE dùng `ghiChuPheDuyet` là không khớp."

- **Action:** BE rename field code dùng đúng snake_case (API có thể nhận camelCase).

### C4. #8 — Mã lỗi `ERR-CTDT-*`

> "Giữ mã lỗi theo SRS dạng `ERR-CTDT-*`. Dev sửa BE nếu đang trả `ERR-STATE-III-01-01`."

- **Action:** BE align error codes; QA update expectations.

### C5. #9 — NHCH 2 trạng thái

> "SRS v3.5 đã chốt 2 trạng thái `KICH_HOAT/VO_HIEU_HOA`. Dòng cũ `NHAP/CONG_KHAI/AN` là lỗi sao chép từ tài liệu cũ **nếu còn xuất hiện ở tài liệu phụ**."

- **Action:** Tech Writer cleanup tài liệu phụ (minor doc edit, không phải SRS update).

### C6. #14 — Form công khai (Khóa học)

> "FE phải bổ sung form công khai, không chỉ hiện xác nhận Có/Không. `thoi_gian_dang_tai` là trường hệ thống tự điền."

- **Action:** FE implement form với 4 trường công khai (theo spec SRS đã có `anh_dai_dien`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`, `cong_khai`).

### C7. #18 — Tên trường từ chối Đợt báo cáo

> "Dùng `ly_do_tu_choi`/`lyDoTuChoi` cho API từ chối. `ghiChuPheDuyet` không thay thế."

- **Action:** BE rename field (giống #6 cho module CT HTPLDN).

### C8. #22 — UI text "24 giờ" sai

> "Liên kết kích hoạt lần đầu là **vĩnh viễn**, dùng 1 lần; liên kết reset password 30 phút. Thông báo UI '24 giờ' sai với SRS."

- **Action:** FE fix UI text label (1-line change).

### C9. #26 — Bỏ tab "Phiên đăng nhập"

> "SRS không mô tả tab này. **Bỏ tab khỏi Profile**. Dev ẩn/xóa UI này; QA không kiểm như tính năng thuộc phạm vi phát hành."

- **Action:** FE remove tab; QA descope test cases.

### C10. #28 — Mã lỗi VAI_TRO + PWD

> "Trong phạm vi SRS v3.5 hiện tại, QA kiểm theo mã trong SRS (`ERR-VT-*`, `ERR-PWD-*`). Dev sửa BE nếu đang dùng mã khác."

- **Action:** BE align error codes (giống #8 cho QTHT module).

### C11. #29 — TVV first-login 401

> "Đây không phải vấn đề đặc tả. Bị 401 sau khi form báo thành công là **lỗi triển khai hoặc lỗi môi trường kiểm thử**. Cần tài khoản TVV/NHT mới, độc lập để kiểm thử."

- **Action:** Dev debug BE token invalidation; QA chuẩn bị fixture TVV mới với password biết.

### C12. #30 — Dấu tiếng Việt thông báo BE

> "Chuẩn i18n: thông báo hiển thị cho người dùng phải có dấu tiếng Việt; log/field/code nội bộ có thể để ASCII. Dev sửa thông báo hướng người dùng, ưu tiên thông báo lỗi workflow/chính sách."

- **Action:** BE i18n cleanup (convert no-dấu → có dấu cho user-facing messages).

---

## 📊 Tổng kết all 30 items

| Nhóm | Số items | Items | Owner | Timeline |
|:-:|:-:|---|---|---|
| **A — BA quyết option** | 4 | #5, #11, #13, #27 | BA | Round 2 BA confirm (1-2 ngày) |
| **B — Update SRS** | 14 | #1, #4, #7, #10, #12, #15, #16, #17, #19, #20, #21, #23, #24, #25 | BA + Tech Writer | SRS v3.6 hoặc patch (1-2 tuần) |
| **C — Implementation/QA align** | 12 | #2, #3, #6, #8, #9, #14, #18, #22, #26, #28, #29, #30 | Dev (BE/FE) + QA | Sprint hiện tại |
| **Tổng** | **30** | | | |

---

## 📌 Lưu ý quan trọng cho QA team Biểu mẫu

| Item | Liên quan đến findings cũ của module Biểu mẫu |
|---|---|
| **B1 (#1)** | Endpoint public cho chuyên trang — liên quan BR-PUBLIC-01/02/03 đã verify trong R7.4.C1. Khi SRS định nghĩa endpoint public, cần test API public mới riêng. |
| **B11 (#21)** | NHT scope BIEU_MAU — giải quyết sub-observation R7.7.10b ("perm-matrix R no asterisk vs impl own-unit"). BA chốt = own-unit + TW dùng chung (NHT thực tế chưa thấy TW dùng chung vì TM TW chưa có cờ `dung_chung`). **Cần re-test BM-035a NHT sau khi SRS update + seed TM TW dùng chung.** |
| **C6 (#14)** | Form công khai Khóa học — pattern tương tự BUG-BM-010 (3 trường công khai). Đã PASS với BM, dev có thể reuse pattern cho Khóa học. |
| **Missing** | **BM-045 spec contradiction (BR-PUBLIC-01 "HUY/TU_CHOI only" vs test plan "AN/HUY")** — KHÔNG có trong file BA này. Cần bổ sung vào BA confirm round 2. |

---

## 🎯 Recommend hành động ngay

1. **Push BA round 2** cho 4 items Nhóm A + 1 item BM-045 (missing) = **5 câu hỏi**:
   - A1 (#5): CT 0/0 đợt báo cáo — chọn Option 1 (thêm cờ) hay Option 2 (đổi message)?
   - A2 (#11): UC nào cho CB NV tạo HV trực tiếp?
   - A3 (#13): Sĩ số tối đa khi DU_THAO — null/0 OK hay luôn `>=1`?
   - A4 (#27): Workflow nào cần dropdown VAI_TRO?
   - **(missing)** BM-045: AN bật Switch công khai — reject hay accept?

2. **Push Tech Writer release SRS v3.6** covering 14 items Nhóm B
   - 5 entity changes (B3/B4/B5/B12/B13)
   - 3 BR mới (B2/B6/B11)
   - 2 API spec (B1/B7)
   - 1 state machine update (B8)
   - 1 API response shape (B10)
   - 1 validation rule (B9)
   - 1 NFR (B14)

3. **Dev/QA sprint** triển khai 12 items Nhóm C song song (không cần chờ BA/SRS):
   - 1 data scoping bug fix (C1)
   - 4 BE/FE alignment fixes (C2/C3/C4/C7/C8/C10)
   - 1 FE form implementation (C6)
   - 1 FE remove tab (C9)
   - 1 doc cleanup (C5)
   - 1 BE i18n (C12)
   - 1 env bug fix (C11)

---

*Phân loại generated 2026-05-12 | QA Automation via Claude Code MCP*
