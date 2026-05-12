# Phân loại follow-up BA — Module Biểu mẫu

**Nguồn:** [`BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md`](BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md)
**File tổng:** [`BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md`](BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md)
**Ngày:** 2026-05-12
**Module:** Biểu mẫu (FR-VII)
**Tổng items:** 1 BA-confirmed + 1 missing (cần bổ sung vào BA round 2)

**Phân loại:**
- **Nhóm A** — Cần BA quyết option (round 2): 1 item (BM-045 missing trong file BA)
- **Nhóm B** — Cần update SRS v3.6: 1 item
- **Nhóm C** — Dev/QA implement trực tiếp: 0 items

---

## 📋 NHÓM A — Cần BA quyết option (1 item — MISSING từ file BA gốc)

### A1. BM-045 — Spec contradiction "AN/HUY reject" vs "HUY/TU_CHOI reject"

⚠️ **Item này KHÔNG có trong file BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11. Cần bổ sung vào BA round 2.**

**Bối cảnh — 2 source spec mâu thuẫn:**

| Source | Quote | Implication |
|---|---|---|
| BR-PUBLIC-01 ([`srs-fr-12-tv-chuyen-sau.md`](../../../../input/srs-update-2026-5-5/srs-fr-12-tv-chuyen-sau.md)) | "Bản ghi Hủy/Từ chối KHÔNG được công khai" | Chỉ reject **HUY/TU_CHOI** (terminal states). AN reversible OK. |
| Test plan BM-045 ([`7.9-bieu-mau.md`](../../../funtion/7.9-bieu-mau.md) line 126) | "`trang_thai=AN/HUY` → bật Switch công khai → reject `ERR-PUBLIC-01`" | Reject cả **AN và HUY**. |

**Phát hiện qua test R8 lần 13 (2026-05-12):**
- Edit BM `ebeac9ac-...` "BM Lao động" trạng thái **AN**
- Toggle Switch OFF→ON → click "Lưu thay đổi"
- Toast "Cập nhật biểu mẫu thành công" ✅ (200 success) — BE **accept** toggle ON cho AN state
- API state sau save: `trangThai=AN, congKhai=true, thoiGianDangTai="2026-05-11T17:59:35Z"` (inconsistent: AN nhưng được công khai)

**Implementation hiện tại:** BE accept theo BR-PUBLIC-01 strict reading (chỉ reject HUY/TU_CHOI, AN OK).

**Cần BA chốt 1 trong 2 path:**

- **Path A (giữ BR-PUBLIC-01):** AN reversible OK, accept toggle Switch ON. Update test plan BM-045 thành "`trang_thai=HUY/TU_CHOI` → reject" (bỏ AN). → BM-045 hiện tại đã ✅ PASS (BE đúng).

- **Path B (giữ BM-045):** AN cũng phải reject. BE add check `trangThai ∈ {AN, HUY, TU_CHOI}` → reject 422 `ERR-PUBLIC-01`. Update BR-PUBLIC-01 thành "Bản ghi AN/Hủy/Từ chối KHÔNG được công khai". → Log BUG-BM-011 Major/Critical.

**Hệ luỵ Path A:** User có thể toggle Switch ON cho BM AN, BM được publish trên Cổng PLQG dù state AN → có thể dẫn đến state lệch UI (list show "Đã ẩn" nhưng vẫn "Công khai" badge).

**Hệ luỵ Path B:** BE chặt chẽ hơn, không lệch state. Đơn giản hóa logic UX (badge "Công khai" chỉ xuất hiện cho BM CONG_KHAI/NHAP).

---

## 📋 NHÓM B — Cần update SRS bổ sung spec (1 item)

### B1. #21 — Quyền NHT/BN/ĐP với BIEU_MAU

> "SRS FR-VII nhiều lần ghi BIEU_MAU/THU_MUC_BIEU_MAU là dữ liệu owned theo `don_vi_id`, query theo `BR-AUTH-08`, 'chỉ xem thư mục thuộc đơn vị mình', 'kết quả matching trong phạm vi đơn vị'. Tuy nhiên BA chốt thêm ngoại lệ nghiệp vụ: BN/ĐP được thấy biểu mẫu dùng chung/cấp TW."

**BA chốt:** Phạm vi đọc BIEU_MAU cho BN/ĐP/NHT **không phải chỉ own-unit thuần**. Quy tắc đúng là:
- Thấy biểu mẫu của đơn vị mình **AND** biểu mẫu cấp TW dùng chung
- KHÔNG thấy biểu mẫu của BN/ĐP ngang cấp khác
- Dev sửa BE nếu đang chỉ trả own-unit
- QA bổ sung case BN/ĐP thấy bản ghi TW nhưng không thấy ngang cấp

**SRS bổ sung:**
- **Cần định nghĩa "biểu mẫu cấp TW dùng chung" cụ thể** — 2 option:
  - **Option (i):** Mọi BM/TM_BM tạo bởi `don_vi.cap = 'TW'` → mặc định dùng chung
  - **Option (ii):** Thêm field `dung_chung: boolean` vào BIEU_MAU/THU_MUC_BIEU_MAU; chỉ khi `dung_chung=true` mới hiển thị cho BN/ĐP/NHT (cần BA confirm thêm)
- Update BR-AUTH-08 cho BIEU_MAU/THU_MUC_BIEU_MAU với rule mới:
  ```
  visible = (don_vi_id = current_user.don_vi_id)
        OR (don_vi.cap = 'TW' AND dung_chung = true)
  ```
- Update FR-VII (Inputs/Processing/AC) phản ánh rule mới
- Update [`permission-matrix.md`](../../../permission-matrix.md) line 534 cho NHT/BN/ĐP với asterisk `R*` (scope conditional)

**Liên quan trực tiếp QA findings R7.7.10b:**
- Verified R8 lần 10: NHT account `nht_01` (STP-AG) chỉ thấy 1 TM = "Biểu mẫu STP-AG - R7.7.10b" (own-unit only, không thấy TM TW gốc)
- Implementation hiện tại = own-unit thuần (theo strict BR-AUTH-08 cũ)
- **Cần re-test BM-035a NHT sau khi SRS update + seed TM TW dùng chung** để verify NHT thấy được TM TW

---

## 📋 NHÓM C — Dev/QA implement trực tiếp (0 items)

Không có item nào của Biểu mẫu thuộc nhóm C.

---

## 📊 Tổng kết Biểu mẫu

| Nhóm | Items | Count |
|:-:|---|:-:|
| **A** | BM-045 (missing) | 1 |
| **B** | #21 | 1 |
| **C** | — | 0 |
| **Tổng** | | **2** |

---

## 🎯 Recommend Biểu mẫu

1. **BA round 2 cho Biểu mẫu:** 1 câu hỏi MỚI cần thêm vào danh sách:
   - **BM-045:** AN bật Switch công khai → accept (Path A) hay reject (Path B)?

2. **SRS v3.6 update cho Biểu mẫu:** 1 item
   - B1 (#21): Định nghĩa rule scope cho BN/ĐP/NHT đọc BIEU_MAU (own-unit + TW dùng chung); thêm cờ `dung_chung` hoặc default-by-TW; update BR-AUTH-08 + FR-VII + permission-matrix line 534

3. **Re-test sau SRS update:**
   - BM-035a NHT scope (sau khi seed TM TW dùng chung)
   - BM-045 (sau khi BA chốt Path A hoặc B)

---

## 📌 Status hiện tại module Biểu mẫu (R7.7.10 + R7.7.10b)

| Task | Status | Note |
|---|:-:|---|
| R7.3.7 Seed | ✅ | |
| R7.4.C1 Workflow | ✅ 8/8 | 6/6 bug closed |
| R7.7.10 Functional 47 TC | ⚠️ | 77% PASS, BM-045 PARTIAL chờ BA |
| R7.7.10b Defer-unblock | ✅ 8/8 | 1/1 bug closed |

**Tổng cộng:** 0 bug open, 1 spec contradiction (BM-045) chờ BA, 1 permission rule (NHT scope) chờ SRS update. Module BM v3.5 essentially production-ready sau khi BA confirm BM-045 + SRS update #21.

---

*Biểu mẫu follow-up | QA Automation 2026-05-12*
