# Bug Report — R7.7.6 DT-054 FE render "Đạt" khi chuyên cần fail (<80%)

> **Module:** Đào tạo / Khóa học / Tab "Kết quả" (FR-III-19 + FR-III-21 BR-KQ-01)
> **Discovered:** 2026-05-12 R12.4 (sau verify DT-054 auto-classify)
> **Reporter:** QA Automation Claude Code MCP

### Severity breakdown

| Tổng | Critical | Major | Medium | Minor | Trivial | Closed | Open |
|------|----------|-------|--------|-------|---------|--------|------|
| 1    | 0        | 1     | 0      | 0     | 0       | 1      | 0    |

## Bug Summary

| ID | Severity | Title | Status |
|---|:-:|---|:-:|
| ~~BUG-DT-054-FE-CHUYEN-CAN-01~~ | Major | Tab "Kết quả" UI render cột "Kết quả" = "Đạt" khi chuyên cần <80% — không match API `ketQua=KHONG_DAT` + vi phạm BR-KQ-01 | **Closed** (R12.5 2026-05-12 22:17 verified — UI render HV04 (chuyên cần 40%, điểm 6.5) = "Không đạt" sync 100% với API `ketQua="KHONG_DAT"`) |

> **🔁 Re-test R12.5 (2026-05-12 22:17, user trigger "verify lại file bug DT-054"):**
>
> Fresh session re-login `cb_nv_tw_01` + navigate KH-005 tab "Kết quả" (`?tab=ket-qua-kiem-tra`). Đối chiếu UI vs API `GET /khoa-hocs/{id}/ket-quas`:
>
> | HV | Chuyên cần | Điểm | API `ketQua` | API `xepLoai` | UI "Kết quả" | Match? |
> |---|---|---|:-:|:-:|:-:|:-:|
> | HV 01 | 5/5 (100%) | 9.5 | DAT | GIOI | Đạt | ✅ |
> | HV 02 | 5/5 (100%) | 7.5 | DAT | KHA | Đạt | ✅ |
> | HV 03 | 4/5 (80%) | 5.5 | DAT | TRUNG_BINH | Đạt | ✅ (border case 80% PASS) |
> | **HV 04** | **2/5 (40%)** | **6.5** | **KHONG_DAT** | **KHONG_DAT** | **Không đạt** | **✅ FIXED** |
> | HV 05 | 5/5 (100%) | 3.5 | KHONG_DAT | KHONG_DAT | Không đạt | ✅ (điểm <5 fail) |
>
> → FE đã update logic compute để check cả `tyLeChuyenCan >= 80%` AND `diemKiemTra >= 5` per BR-KQ-01, hoặc đọc trực tiếp `record.ketQua` từ API. Test case quan trọng (HV04 chuyên cần fail) đã render đúng "Không đạt". Border case HV03 (chuyên cần đúng 80%) cũng đúng "Đạt". Screenshot: [r12-5-dt054-fe-chuyen-can-fixed-hv04-khong-dat.png](image/r12-5-dt054-fe-chuyen-can-fixed-hv04-khong-dat.png).

---

## BUG-DT-054-FE-CHUYEN-CAN-01

### Mô tả

Tab "Kết quả" trong trang chi tiết Khóa học hiển thị cột "Kết quả" sai cho HV có chuyên cần dưới 80%. FE compute kết quả chỉ dựa vào `diemKiemTra >= 5` mà KHÔNG check `tyLeChuyenCan >= 80%` theo spec BR-KQ-01. API trả `ketQua: "KHONG_DAT"` đúng, nhưng UI render "Đạt".

### Bước tái hiện

1. Login `cb_nv_tw_01` / `Secret@123` / OTP `666666`.
2. Navigate `/dao-tao/khoa-hoc/929c53ba-b9f6-4ffa-874d-791072cc803e` (KH-20260509-005 "Sở hữu trí tuệ cho startup - R9", state DA_KET_THUC).
3. Click tab "Kết quả".
4. Đối chiếu cột "Kết quả" giữa UI và API response.

### Kết quả mong đợi (BR-KQ-01 + BR-KQ-02)

Cột "Kết quả" hiển thị "Không đạt" cho HV có chuyên cần <80% (bất kể điểm), match đúng `ketQua` trong API response `GET /khoa-hocs/{id}/ket-quas`.

### Kết quả thực tế

| HV | Chuyên cần | Điểm | API `ketQua` | UI "Kết quả" | Match? |
|---|---|---|:-:|:-:|:-:|
| QA R7 HV 01 | 5/5 (100%) | 9.5 | DAT | Đạt | ✅ |
| QA R7 HV 02 | 5/5 (100%) | 7.5 | DAT | Đạt | ✅ |
| QA R7 HV 03 | 4/5 (80%) | 5.5 | DAT | Đạt | ✅ |
| **QA R7 HV 04** | **2/5 (40%)** | 6.5 | **KHONG_DAT** | **Đạt** | ❌ |
| QA R7 HV 05 | 5/5 (100%) | 3.5 | KHONG_DAT | Không đạt | ✅ |

**HV 04** chuyên cần 40% (<80% threshold) → API `ketQua=KHONG_DAT` đúng spec, **UI render "Đạt" sai**.

### Bằng chứng

- Screenshot UI tab "Kết quả": [image/r12-dt054-ui-chuyen-can-fail-render-dat.png](image/r12-dt054-ui-chuyen-can-fail-render-dat.png)
- DOM extract row 4: `["4", "QA R7 HV 04", "2/5 (40%)", "", "Đạt", ""]` (cột 5 = "Đạt")
- API `GET /api/v1/khoa-hocs/929c53ba-b9f6-4ffa-874d-791072cc803e/ket-quas` row 4: `{"hoTen":"QA R7 HV 04", "tyLeChuyenCan":40, "diemKiemTra":6.5, "ketQua":"KHONG_DAT", "xepLoai":"KHONG_DAT"}`

### So sánh

| Source | Logic compute kết quả |
|---|---|
| **BE** (BR-KQ-01) | `ketQua = KHONG_DAT` nếu `tyLeChuyenCan < 80%` HOẶC `diemKiemTra < 5`; ngược lại `DAT`. |
| **FE** (UI bug) | `ketQua = DAT` nếu `diemKiemTra >= 5` — bỏ qua `tyLeChuyenCan` check. |

**Spec ref:** `srs-update-2026-5-5/srs-fr-03-dao-tao.md` FR-III-21 BR-KQ-01 (chuyên cần >=80% là điều kiện cần để DAT).

**Impact:** Trainer/admin/DN/HV đọc UI thấy HV04 "Đạt" → ra quyết định sai (cấp chứng chỉ / công bố). Phải override bằng cách look at xếp loại column hoặc API direct → trải nghiệm tệ + risk nhầm lẫn business.

**Severity:** Major (sai data hiển thị quan trọng + ảnh hưởng quyết định business, không phải UI cosmetic).

**Recommend fix FE:**
```js
// Trong table cell render Kết quả
const ketQua = (record.tyLeChuyenCan >= 80 && record.diemKiemTra >= 5) ? 'Đạt' : 'Không đạt';
// HOẶC dùng trực tiếp record.ketQua từ API:
const ketQua = record.ketQua === 'DAT' ? 'Đạt' : 'Không đạt';
```

→ Recommend lựa chọn 2 (đọc trực tiếp `record.ketQua` từ BE để tránh duplicate logic FE/BE drift).
