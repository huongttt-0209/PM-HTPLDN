# Phân loại follow-up BA — Module CT HTPLDN

**Nguồn:** [`BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md`](BA-CONFIRM-ANSWERS-4-MODULE-2026-05-11.md)
**File tổng:** [`BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md`](BA-FOLLOWUP-CLASSIFICATION-2026-05-12.md)
**Ngày:** 2026-05-12
**Module:** CT HTPLDN — Chương trình HTPLDN + Đợt báo cáo (FR-XI)
**Tổng items:** 5

**Phân loại:**
- **Nhóm A** — Cần BA quyết option (round 2): 1 item
- **Nhóm B** — Cần update SRS v3.6: 3 items
- **Nhóm C** — Dev/QA implement trực tiếp: 1 item

---

## 📋 NHÓM A — Cần BA quyết option (1 item)

### A1. #5 — CT HTPLDN hoàn thành "0/0 đợt báo cáo"

> "SRS FR-XI-01 ghi điều kiện hoàn thành CT là 'tất cả đợt báo cáo đã hoàn thành'; SM-KH-CTHTPL cũng ghi `DANG_THUC_HIEN → HOAN_THANH` khi 'Tất cả đợt BC hoàn thành'. SRS **không nói CT bắt buộc phải có tối thiểu 1 đợt báo cáo**. Vì vậy trường hợp 0 đợt báo cáo là khoảng trống đặc tả."

**BA propose 2 option chưa chốt:**
- **Option 1:** Thêm field `khong_yeu_cau_bao_cao: boolean` vào entity CHUONG_TRINH_HTPL + UI checkbox khi tạo CT
  - Rule: `HOAN_THANH` được phép khi `(khong_yeu_cau_bao_cao = true) OR (COUNT(DOT_BAO_CAO) > 0 AND ALL DOT_BAO_CAO.trang_thai = DA_TONG_HOP)`
- **Option 2:** Không thêm field, mọi CT bắt buộc ≥1 đợt báo cáo; chỉ đổi message error
  - Thông báo đúng: "Chương trình chưa có đợt báo cáo để xác nhận hoàn thành" (thay vì "0/0 chưa DA_TONG_HOP")

→ **Cần BA chốt:** Option 1 hay Option 2?

---

## 📋 NHÓM B — Cần update SRS bổ sung spec (3 items)

### B1. #17 — Transition TW `DA_DUYET_KQ → DA_TONG_HOP`

> "SRS SM-DOT-BC hiện chỉ có `DA_DUYET_KQ → DA_GUI_TW → DA_TONG_HOP`; FR-XI-08 actor BN/ĐP, FR-XI-09 tổng hợp báo cáo từ BN/ĐP đã gửi. Chưa có đường trực tiếp cho đợt báo cáo cấp TW."

**BA chốt:** Thêm chuyển trạng thái riêng cho TW: `DA_DUYET_KQ → DA_TONG_HOP` khi đợt báo cáo thuộc TW và CB NV TW xác nhận tổng hợp/nội bộ. BN/ĐP vẫn phải qua `DA_GUI_TW`.

**SRS bổ sung:**
- Update SM-DOT-BC (state machine Đợt báo cáo):
  - Thêm transition: `DA_DUYET_KQ → DA_TONG_HOP` (chỉ áp dụng khi đợt BC thuộc cấp TW)
  - Guard condition: `dot_bao_cao.don_vi.cap = 'TW'`
  - Actor: CB NV TW
- FR-XI-09 hoặc FR-XI mới: spec action "Xác nhận tổng hợp nội bộ TW"
- BN/ĐP vẫn phải qua `DA_GUI_TW` như cũ

### B2. #19 — `/start` cho phép `soLieuTongHop.fields` rỗng

> "FR-XI-06 mô tả lập báo cáo theo mẫu 21a/21b và SM-DOT-BC chốt điều kiện `DANG_LAP_BC → CHO_DUYET_KQ` là 'BC đầy đủ số liệu'. SRS không nói rõ validation tại bước `/start` phải có tối thiểu 1 trường số liệu."

**BA chốt:** `/start` được tạo khung báo cáo rỗng, nhưng khi trình duyệt phải kiểm tra `soLieuTongHop.fields` không rỗng và đủ trường bắt buộc theo mẫu.

**SRS bổ sung:**
- FR-XI-06 làm rõ "POST /start: fields có thể rỗng (chỉ tạo khung)"
- Validation chuyển sang bước `DANG_LAP_BC → CHO_DUYET_KQ`:
  - Kiểm `soLieuTongHop.fields` non-empty
  - Đủ trường bắt buộc theo mẫu 21a/21b
- Error message khi thiếu data: "Báo cáo chưa đủ số liệu để trình duyệt"

### B3. #20 — Response `POST /tong-hop` đổi shape

> "FR-XI-09 input `bao_cao_ids` là danh sách và output là 'BC tổng hợp TW' + các đợt BC được chọn chuyển sang `DA_TONG_HOP`. Nếu response chỉ có `dotBaoCaoId` dạng đơn thì thiết kế không phù hợp với use case chọn nhiều báo cáo."

**BA chốt:** Đổi response thành `dotBaoCaoIds: []`, `baoCaoTongHopId`, `soDotTongHop`.

**SRS bổ sung:**
- FR-XI-09 Outputs update:
  - Trước: `dotBaoCaoId` (đơn)
  - Sau: `{dotBaoCaoIds: UUID[], baoCaoTongHopId: UUID, soDotTongHop: number}`
- Update `danh-sach-api.md` với response shape mới
- BE migration: backward compatibility nếu cần

---

## 📋 NHÓM C — Dev/QA implement trực tiếp (1 item)

### C1. #18 — Tên trường từ chối Đợt báo cáo

> "FR-XI-07a input/output dùng `ly_do`; thông báo nói 'lý do từ chối'; DB/BE có thể dùng `ghiChuPheDuyet`. SRS chưa chuẩn hóa tên trường."

**BA chốt:** Dùng `ly_do_tu_choi` / `lyDoTuChoi` cho API từ chối. `ghiChuPheDuyet` nếu tồn tại chỉ nên là ghi chú duyệt chung, không thay thế lý do từ chối.

- **Action:** BE rename field code dùng đúng `ly_do_tu_choi` (snake_case DB / `lyDoTuChoi` camelCase API); không tái sử dụng `ghiChuPheDuyet` cho lý do từ chối

---

## 📊 Tổng kết CT HTPLDN

| Nhóm | Items | Count |
|:-:|---|:-:|
| **A** | #5 | 1 |
| **B** | #17, #19, #20 | 3 |
| **C** | #18 | 1 |
| **Tổng** | | **5** |

---

## 🎯 Recommend CT HTPLDN

1. **BA round 2 cho CT HTPLDN:** 1 câu hỏi (#5 CT 0/0 đợt BC — Option 1 hay 2?)
2. **SRS v3.6 update cho CT HTPLDN:** 3 items
   - 1 state machine update (B1 SM-DOT-BC thêm transition TW)
   - 1 validation rule clarification (B2 /start cho phép rỗng)
   - 1 API response shape (B3 POST /tong-hop trả mảng)
3. **Dev/QA sprint CT HTPLDN:** 1 item (BE rename field từ chối)

---

*CT HTPLDN follow-up | QA Automation 2026-05-12*
