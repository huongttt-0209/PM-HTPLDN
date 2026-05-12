# Phân loại follow-up BA — Module Đào tạo

**Nguồn:** [`BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md`](BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md)
**File tổng:** [`BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md`](BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md)
**Ngày:** 2026-05-12
**Module:** Đào tạo (FR-III + FR-XII + FR-16 inbound)
**Tổng items:** 15

**Phân loại:**
- **Nhóm A** — Cần BA quyết option (round 2): 2 items
- **Nhóm B** — Cần update SRS v3.6: 7 items
- **Nhóm C** — Dev/QA implement trực tiếp: 6 items

---

## 📋 NHÓM A — Cần BA quyết option (2 items)

### A1. #11 — Điểm vào tạo Học viên

> "CMS CB NV chỉ duyệt/quản lý... không tạo HV thay DN **trừ khi có UC bổ sung**."

- **Cần BA xác nhận:** Có UC nào cho CB NV tạo HV trực tiếp không? Nếu có thì UC nào? Nếu không → endpoint `POST /hoc-viens` chỉ là admin/seed, Dev tắt UI/permission cho CB NV.

### A2. #13 — Sĩ số tối đa khi DU_THAO

> "Bắt buộc `so_luong_toi_da >= 1` trước khi `DU_THAO → CHO_DUYET`. **Có thể cho phép** bỏ trống khi lưu nháp."

- **Cần BA quyết hẳn:**
  - Option 1: DU_THAO cho phép `null/0`; chỉ validate `>=1` khi chuyển CHO_DUYET
  - Option 2: Luôn bắt buộc `>=1` ngay từ lưu nháp (BE constraint đã ép sẵn)

---

## 📋 NHÓM B — Cần update SRS bổ sung spec (7 items)

### B1. #1 — Endpoint public cho chuyên trang Cổng PLQG

> "Với FR-III-04/UC23, DN/NHT đăng ký học viên qua chuyên trang phải đi qua API/chức năng public... Dev không dùng API CMS có VPD nội bộ rồi yêu cầu 'bypass'. Cần tách endpoint public hoặc bổ sung rõ rule."

**SRS bổ sung:**
- URL pattern: `/api/public/dao-tao/khoa-hoc/danh-sach` (hoặc tương tự) — tách rõ khỏi `/api/v1/khoa-hocs` (CMS)
- Authentication: không cần JWT CMS, có thể public hoặc mTLS từ Cổng PLQG
- Filter rule: chỉ trả `cong_khai=true AND trang_thai IN (DA_CONG_KHAI, DANG_DIEN_RA) AND deleted_at IS NULL`
- Section public API riêng trong FR-III + FR-16

### B2. #4 — Đề kiểm tra: không cần duyệt + quy tắc xóa

> "Không cần phê duyệt riêng. 'Chưa sử dụng' để xóa là: chưa `DA_PHAN_PHOI` **AND** chưa có `KET_QUA_DAO_TAO.de_kiem_tra_id` liên kết."

**SRS bổ sung:**
- FR-III-NEW-01/02/03 thêm BR rõ "không có workflow duyệt"
- Định nghĩa "chưa sử dụng" để xóa (2 điều kiện AND)
- Entity `DE_KIEM_TRA` giữ 4 trạng thái: `DU_THAO`, `DA_PHAN_PHOI`, `HOAN_THANH`, `HUY` (không thêm `CHO_DUYET`/`DA_DUYET`)

### B3. #7 — 3 field từ chối kết quả đào tạo

> "Bổ sung trường riêng cho từ chối kết quả: `ly_do_tu_choi_kq`, `thoi_gian_tu_choi_kq`, `nguoi_tu_choi_kq`. Không dùng chung `ly_do_tu_choi` của bước phê duyệt Khóa học."

**SRS bổ sung:**
- Entity `KHOA_HOC` thêm 3 column:
  - `ly_do_tu_choi_kq` VARCHAR(500) NULL
  - `thoi_gian_tu_choi_kq` TIMESTAMP NULL
  - `nguoi_tu_choi_kq` UUID NULL FK NGUOI_DUNG
- FR-III-18 Inputs/Outputs/Processing update tham chiếu 3 field này
- Migration DB

### B4. #10 — Tài khoản HOC_VIEN không bắt buộc

> "`taiKhoanId` của HOC_VIEN là **không bắt buộc**, HV được quản lý dưới TK DN/NHT đã đăng ký. Không tự tạo TAI_KHOAN cho từng học viên."

**SRS bổ sung:**
- Entity `HOC_VIEN.tai_khoan_id` NULL allowed
- FR-III-19 làm rõ "HV không có TK riêng, xem kết quả qua tài khoản DN/NHT"
- BR-AUTH-USERNAME-01 confirm không có convention sinh username cho HV
- Không mở actor "Học viên" độc lập

### B5. #12 — Hình thức Khóa học `KET_HOP`

> "Thêm enum `KET_HOP` cho `KHOA_HOC.hinh_thuc`. Khi `KET_HOP`, từng `LICH_HOC.hinh_thuc_buoi` bắt buộc chọn `TRUC_TUYEN`/`TRUC_TIEP`."

**SRS bổ sung:**
- Entity `KHOA_HOC`: update CHECK constraint `hinh_thuc IN ('TRUC_TUYEN', 'TRUC_TIEP', 'KET_HOP')`
- Entity `LICH_HOC`: bổ sung field `hinh_thuc_buoi` (TRUC_TUYEN/TRUC_TIEP)
- BR: khi `KHOA_HOC.hinh_thuc = KET_HOP` thì `LICH_HOC.hinh_thuc_buoi` NOT NULL
- FR-III-22 Inputs validation rule

### B6. #15 — Quy tắc chống trùng lịch học `BR-LH-CONFLICT-01`

> "Bổ sung `BR-LH-CONFLICT-01` vào FR-III-22: không cho tạo/sửa buổi học trùng khoảng thời gian trong cùng Khóa học."

**SRS bổ sung:**
- Thêm BR mới `BR-LH-CONFLICT-01` vào FR-III-22 §Business Rules:
  - Khi tạo/sửa `LICH_HOC`, kiểm tra không tồn tại `LICH_HOC` khác cùng `khoa_hoc_id` mà có khoảng `[thoi_gian_bat_dau, thoi_gian_ket_thuc]` overlap
  - Error code: `ERR-LH-CONFLICT-01` "Buổi học bị trùng thời gian với buổi học khác trong cùng khóa"
- Tương lai (defer): mở rộng theo `giang_vien_id` khi quản lý lịch giảng viên

### B7. #16 — 2 API inbound từ Cổng PLQG

> "DN/NHT đăng ký đào tạo từ Cổng PLQG là yêu cầu sản phẩm. SRS đang thiếu API tiếp nhận. BA/SRS cần bổ sung endpoint inbound riêng."

**SRS bổ sung trong FR-16:**

**(a) API tiếp nhận đăng ký đào tạo:**
- Path: `POST /api/inbound/cong-plqg/dang-ky-dao-taos`
- Auth: mTLS + JWT từ Cổng PLQG
- Request: `{maCongPLQG, hoTen, email, soDienThoai, khoaHocId, donViDangKy, ...}`
- Response: `{maDangKyNoiBo, trangThai: 'CHO_DUYET'}`
- Anti-duplicate: idempotency key
- Tạo record `DANG_KY_DAO_TAO`

**(b) API tiếp nhận/thêm học viên theo đăng ký:**
- Path: `POST /api/inbound/cong-plqg/hoc-viens`
- Auth: mTLS + JWT
- Request: list HV info + `dangKyId`
- Response: list `{hocVienId, trangThai}`
- Validation: kiểm tra khóa học public + scope đăng ký + required fields

**KHÔNG dùng tạm endpoint CMS nội bộ cho luồng này.**

---

## 📋 NHÓM C — Dev/QA implement trực tiếp (6 items)

### C1. #2 — Lộ data KH năm xuyên đơn vị

> "SRS chốt rõ FR-III-14 Processing bước 2 lấy `KE_HOACH_DAO_TAO` thuộc đơn vị. BR-AUTH-03/04: BN/ĐP không thấy data ngang cấp; TW thấy TW+BN+ĐP. Nếu API đang trả 7 bản ghi từ 3 `donViId` cho BN/ĐP thì đó là **lỗi lộ dữ liệu**, không phải điểm mơ hồ của SRS."

- **Action:** Dev fix BE bug (apply BR-AUTH-03/04/08 đúng); QA verify scope per role:
  - CB NV/PD TW: toàn quốc (TW + BN + ĐP)
  - CB NV/PD BN: chỉ BN mình
  - CB NV/PD ĐP: chỉ ĐP mình
- BR-AUTH-05 cho CB PD duyệt vẫn phải đúng đơn vị, không duyệt hộ cấp dưới

### C2. #3 — Khóa học 9 trạng thái

> "SRS v3.5 đã chốt **9 trạng thái** (không phải 11), không có `TU_CHOI` riêng. Khi từ chối: `CHO_DUYET → DU_THAO` + ghi `ly_do_tu_choi`, `thoi_gian_tu_choi`, `nguoi_tu_choi`. Nếu BE/UI hiện chỉ có khoảng 6 trạng thái thì BE/UI đang thiếu các trạng thái sau duyệt, công khai, kết thúc, chờ duyệt kết quả, hoàn thành/hủy."

- **Danh sách chuẩn 9 trạng thái:** `DU_THAO`, `CHO_DUYET`, `DA_DUYET`, `DA_CONG_KHAI`, `DANG_DIEN_RA`, `DA_KET_THUC`, `CHO_DUYET_KQ`, `HOAN_THANH`, `DA_HUY`
- **Action:** BE/UI implement đủ 9 trạng thái theo SRS; QA update test cases

### C3. #6 — Tên trường lý do từ chối (Đào tạo)

> "SRS Đào tạo dùng bộ trường riêng `ly_do_tu_choi`, `thoi_gian_tu_choi`, `nguoi_tu_choi` cho Kế hoạch năm, CTĐT và Khóa học. BE dùng `ghiChuPheDuyet` là không khớp SRS. API có thể nhận camelCase (`lyDoTuChoi`) nhưng DB/SRS giữ tên chuẩn snake_case."

- **Action:** BE rename field code dùng đúng snake_case; không tái sử dụng `ghiChuPheDuyet` cho lý do từ chối

### C4. #8 — Mã lỗi `ERR-CTDT-*`

> "SRS FR-III-01 khai báo mã lỗi theo nghiệp vụ (`ERR-CTDT-*`, `ERR-KH-PD-*`). Nếu BE trả `ERR-STATE-III-01-01` thì lệch quy ước hiện có. Giữ mã lỗi theo SRS dạng `ERR-CTDT-*` cho CTĐT. Không để hai mã lỗi cho cùng một tình huống."

- **Action:** BE align error codes về `ERR-CTDT-*`; QA update expectations

### C5. #9 — Ngân hàng câu hỏi 2 trạng thái

> "SRS v3.5 đã chốt nguồn đúng là **2 trạng thái** `KICH_HOAT/VO_HIEU_HOA`. Dòng cũ `NHAP/CONG_KHAI/AN` là lỗi sao chép từ tài liệu cũ nếu còn xuất hiện ở tài liệu phụ."

- **Action:** Tech Writer cleanup tài liệu phụ nếu còn dòng cũ; BE/UI follow SRS chính

### C6. #14 — Hộp thoại "Công khai khóa học"

> "SRS yêu cầu các trường công khai chung cho CTĐT/Khóa học: `anh_dai_dien`, `thoi_gian_dang_tai`, `mo_ta_cong_khai`, `file_dinh_kem_cong_khai`, `cong_khai`. FE phải bổ sung form công khai, không chỉ hiện xác nhận Có/Không. `thoi_gian_dang_tai` là trường hệ thống tự điền, người dùng không nhập."

- **Action:** FE implement form với 4 trường công khai (theo spec SRS đã có)
- **Note:** Pattern tương tự BUG-BM-010 đã PASS với module Biểu mẫu — Dev có thể reuse pattern (`Form.useWatch('cong_khai')` + conditional render)

---

## 📊 Tổng kết Đào tạo

| Nhóm | Items | Count |
|:-:|---|:-:|
| **A** | #11, #13 | 2 |
| **B** | #1, #4, #7, #10, #12, #15, #16 | 7 |
| **C** | #2, #3, #6, #8, #9, #14 | 6 |
| **Tổng** | | **15** |

---

## 🎯 Recommend Đào tạo

1. **BA round 2 cho Đào tạo:** 2 câu hỏi (#11 UC tạo HV, #13 sĩ số DU_THAO)
2. **SRS v3.6 update cho Đào tạo:** 7 items
   - 2 entity changes (B3 KHOA_HOC + B5 LICH_HOC)
   - 2 BR mới (B2 đề kiểm tra + B6 chống trùng lịch)
   - 2 API spec (B1 public endpoint + B7 inbound từ Cổng PLQG)
   - 1 entity update (B4 HOC_VIEN.tai_khoan_id NULL)
3. **Dev/QA sprint Đào tạo:** 6 items implement song song

---

*Đào tạo follow-up | QA Automation 2026-05-12*
