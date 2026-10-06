# Test Cases — FR-II-08 + FR-II-09 (UC17+UC18): Phê duyệt + Công khai + Đã xử lý

> **SRS Ref**: FR-II-08 (lines 631-779), FR-II-09 (lines 782-841), SCR-II-02 dòng 14-18 (Phê duyệt/Từ chối/Công khai/Hủy CK/Đóng hồ sơ), SCR-II-01 tab "Chờ phê duyệt" + "Đã duyệt" + "Công khai" + "Hoàn thành" với batch action-bar 34-35
> **Ngày tạo**: 2026-05-10
> **Đặc thù**:
> - **Phê duyệt**: state CHO_PHE_DUYET → DA_DUYET, chỉ CB PD cùng cấp (BR-AUTH-05).
> - **Từ chối**: state CHO_PHE_DUYET → DANG_XU_LY, ly_do 10-1000 ký bắt buộc (BR-FLOW-04).
> - **Công khai**: state DA_DUYET → CONG_KHAI, **lock TTL 30s + flag `api_in_progress`** (F-42), API trực tiếp Cổng PLQG. KHÔNG set CONG_KHAI trước khi API OK (EC-04, BR-EC-20). Idempotency key chống duplicate.
> - **Hủy công khai**: state CONG_KHAI → DA_DUYET, gỡ qua API + lock TTL 30s.
> - **Đóng hồ sơ**: state DA_DUYET/CONG_KHAI → HOAN_THANH, **THỦ CÔNG** (BR-FLOW-06, BA chốt 2026-05-05). KHÔNG auto-close.
> - **Phê duyệt hàng loạt**: max 100 records/batch (BR-EC-19, ERR-PD-05). Per-record với optimistic locking + báo cáo per-record.
> - **FR-II-09 Đã xử lý**: read-only (BR-FLOW-03), tab "Hoàn thành".
> - **EC-01 Auto-escalate**: CHO_PHE_DUYET >3 ngày LV không xử lý → in-app + email + escalate.

---

## Quy ước

- **Priority**: 🔴 P0 · 🟡 P1 · 🟢 P2
- **TraceID**: `FR-II-08 / {section}` hoặc `FR-II-09 / {section}`
- **Pre-conditions**: User CB_PD_{cap} cùng cấp (`user.don_vi.cap = record.don_vi.cap`, BR-AUTH-05).

---

## Trường input

**Phê duyệt** (chỉ hoi_dap_id):

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |

**Từ chối**:

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | URL/system |
| 2 | ly_do_tu_choi | Y | text long | Min 10, max 1000 ký, plain text |

**Công khai**:

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_id | Y | identifier | State DA_DUYET |
| 2 | anh_dai_dien | N | file | jpg/png/gif, max 5MB. Default ảnh hệ thống |
| 3 | mo_ta_cong_khai | N | text long | Max 2000 ký (đếm plain text sau XSS sanitize), HTML sanitize F-38 |
| 4 | file_dinh_kem_cong_khai | N | file[] | PDF/DOC/DOCX/XLS/XLSX, max 20MB/file, max 10 file, ClamAV |

**Phê duyệt hàng loạt**:

| # | Field | Bắt buộc | Kiểu | Ràng buộc |
|---|-------|----------|------|-----------|
| 1 | hoi_dap_ids[] | Y | identifier[] | Max 100 records (BR-EC-19) |

---

## A. PHÊ DUYỆT — HAPPY

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-001 | FR-II-08 / Processing Phê duyệt + AC #2 | CB PD phê duyệt single — happy | cb_pd_tw_01 login. HD-X state CHO_PHE_DUYET, scope TW. | — | 1. SCR-II-02 HD-X. 2. Click [Phê duyệt] dòng 14. 3. C12 confirm. | (1) PUT /hoi-dap/{id}/phe-duyet thành công. (2) State badge → "Đã duyệt" (xanh lá đậm). (3) HD: `trang_thai=DA_DUYET`, `nguoi_duyet_id=cb_pd_tw_01`, `ngay_duyet=NOW()`. (4) Notification in-app cho CB NV soạn phản hồi. Audit log INSERT action='PHE_DUYET'. | Happy 🔴 |
| TC-PD-002 | FR-II-08 / Tab Chờ phê duyệt + Auto-active | CB PD vào SCR-II-01 → tab "Chờ phê duyệt" mặc định active | cb_pd_tw_01 login. ≥3 HD CHO_PHE_DUYET scope TW. | — | 1. Truy cập SCR-II-01 (cb_pd_tw_01). | (3) Tab "Chờ phê duyệt" highlight active mặc định (gộp MH-02.4 v2.1). Badge đỏ số lượng "(3)". Bảng hiển thị 3 records. | Happy 🟡 |

---

## B. TỪ CHỐI — HAPPY + NEGATIVE (BR-FLOW-04)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-010 | FR-II-08 / Processing Từ chối + BR-FLOW-04 | Từ chối với lý do hợp lệ | cb_pd_tw_01 login. HD-Y CHO_PHE_DUYET. CB NV soạn ban đầu = cb_nv_tw_01. | ly_do="Phản hồi chưa đầy đủ căn cứ pháp lý, đề nghị bổ sung Điều 5 NĐ X" (84 ký) | 1. SCR-II-02 HD-Y. 2. Click [Từ chối] dòng 15. 3. Modal mở textarea ly_do counter `{n}/1000`. 4. Nhập lý do. 5. Click [Xác nhận từ chối]. | (1) PUT /hoi-dap/{id}/tu-choi thành công. (3) HD: `trang_thai=DANG_XU_LY` (trả về CB NV). PHAN_HOI: `ly_do_tu_choi` lưu. (4) Notification in-app + email cho cb_nv_tw_01 kèm lý do. Audit log action='TU_CHOI'. | Happy 🔴 |
| TC-PD-011 | FR-II-08 / E2 ERR-PD-02 | Từ chối thiếu lý do | cb_pd_tw_01 login. HD-Z CHO_PHE_DUYET. | ly_do="" | 1. Modal mở. 2. Bỏ trống. 3. Submit. | (2) Inline error: **"Vui lòng nhập lý do từ chối"** (ERR-PD-02). | Negative 🔴 |
| TC-PD-012 | FR-II-08 / E2 ERR-PD-02 | Từ chối ly_do < 10 ký | cb_pd_tw_01 login. HD-W CHO_PHE_DUYET. | ly_do="ngắn" (5 ký) | 1. Nhập 5 ký. 2. Submit. | (2) Inline error: **"Lý do phải có ít nhất 10 ký tự"** (BR-FLOW-04 enforce). | Negative 🟡 |
| TC-PD-013 | FR-II-08 / E2 ERR-PD-02 | Từ chối ly_do > 1000 ký | cb_pd_tw_01 login. HD-V CHO_PHE_DUYET. | ly_do=1001 ký | 1. Paste. 2. Counter `1001/1000` đỏ. | (2) Counter đỏ + nút disabled HOẶC submit reject. | Negative 🟢 |

---

## C. PHÊ DUYỆT — NEGATIVE (BR-AUTH-05 cùng cấp)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-100 | FR-II-08 / E1 ERR-PD-01 + BR-AUTH-05 | CB PD khác cấp attempt phê duyệt | HD-U CHO_PHE_DUYET scope ĐP (Sở TP AG). cb_pd_tw_01 login. | — | 1. cb_pd_tw_01 mở SCR-II-02 HD-U (qua URL hoặc danh sách). | (2) Nút [Phê duyệt] KHÔNG hiển thị (BR-AUTH-05 cùng cấp: TW ≠ ĐP). Force PUT API → ERR-PD-01 **"Bạn không có quyền phê duyệt bản ghi thuộc đơn vị khác cấp"**. | Negative 🔴 |
| TC-PD-101 | FR-II-08 / E3 ERR-PD-03 | Phê duyệt state ≠ CHO_PHE_DUYET | cb_pd_tw_01 login. HD-T state DANG_XU_LY. | — | 1. Mở SCR-II-02. | (2) Nút [Phê duyệt] KHÔNG hiển thị (state ≠ CHO_PHE_DUYET). Force API → ERR-PD-03 **"Hỏi đáp không ở trạng thái chờ phê duyệt"**. | Negative 🟡 |
| TC-PD-102 | FR-II-08 / Permission CB_NV | CB_NV attempt phê duyệt | cb_nv_tw_01 login. HD-S CHO_PHE_DUYET scope TW. | — | 1. Mở SCR-II-02. | (2) Nút [Phê duyệt] KHÔNG hiển thị (chỉ CB_PD). | Negative 🟡 |

---

## D. CÔNG KHAI — HAPPY + NEGATIVE (BR-FLOW-05 + EC-04 + F-42)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-020 | FR-II-08 / Công khai happy + BR-EC-20 | Công khai DA_DUYET → CONG_KHAI (API Cổng OK) | cb_pd_tw_01 login. HD-R DA_DUYET scope TW. Mock API Cổng PLQG OK. | mo_ta_cong_khai="Công khai trên Cổng PLQG" (35 ký), anh_dai_dien=ảnh hệ thống mặc định | 1. SCR-II-02 HD-R. 2. Click [Công khai] dòng 16. 3. Modal mở (ref F-08): upload ảnh + textarea mô tả + file đính kèm + preview. 4. Nhập mo_ta. 5. Click [Xác nhận công khai]. | (1) Lock record TTL 30s + `api_in_progress=true`. (2) PUT API Cổng PLQG (idempotency key). (3) API OK → release lock + SET HD: `trang_thai=CONG_KHAI`, `cong_khai=1`, `thoi_gian_dang_tai=NOW()`, `nguoi_cong_khai_id=cb_pd_tw_01`. (4) Audit log action='CONG_KHAI' kèm input fields + API status. | Happy 🔴 |
| TC-PD-021 | FR-II-08 / EC-04 + ERR-PD-04 | Công khai API Cổng FAIL → giữ DA_DUYET | cb_pd_tw_01 login. HD-Q DA_DUYET. Mock API Cổng PLQG trả 503. | — | 1. Mở modal. 2. Submit. | (1) Lock + API call. (2) API fail → release lock + GIỮ HD state DA_DUYET (KHÔNG set CONG_KHAI per BR-EC-20/EC-04). (3) Toast persistent: **"Lỗi kết nối Cổng Pháp luật Quốc gia. Vui lòng thử công khai lại"** (ERR-PD-04). Phân biệt: timeout / 5xx / business — kèm nút "Thử lại". (4) Audit log full request/response. | Negative 🔴 |
| TC-PD-022 | FR-II-08 / Hủy công khai happy | Hủy công khai CONG_KHAI → DA_DUYET (API gỡ OK) | cb_pd_tw_01 login. HD-P CONG_KHAI. Mock API gỡ OK. | — | 1. SCR-II-02 HD-P. 2. Click [Hủy công khai] dòng 17. 3. C12 "Gỡ khỏi Cổng PLQG?". 4. Confirm. | (1) Lock TTL 30s. (2) API gỡ OK → release lock + SET HD: `trang_thai=DA_DUYET`, `cong_khai=0`, `clear thoi_gian_dang_tai`. (3) Audit log action='HUY_CONG_KHAI'. | Happy 🔴 |
| TC-PD-023 | FR-II-08 / E6 ERR-PD-06 | Hủy công khai API fail → giữ CONG_KHAI | cb_pd_tw_01 login. HD-O CONG_KHAI. Mock API gỡ trả 500. | — | 1. Click [Hủy công khai]. | (2) Toast persistent ERR-PD-06: **"Lỗi kết nối Cổng Pháp luật Quốc gia khi hủy. Vui lòng thử lại"** + nút Thử lại. State giữ CONG_KHAI. | Negative 🟡 |
| TC-PD-024 | FR-II-08 / E7 ERR-PD-07 + F-42 (race) | 2 user concurrent Công khai vs Hủy CK trên cùng record | cb_pd_tw_01 + cb_pd_tw_02 cùng login. HD-N DA_DUYET. | — | 1. cb_pd_tw_01 click [Công khai] → modal mở → submit → lock acquired. 2. **Trong lúc lock chưa release**, cb_pd_tw_02 click [Công khai] cùng record. | (2) cb_pd_tw_02 nhận ERR-PD-07 **"Đang có thao tác Công khai/Hủy công khai khác đang xử lý trên bản ghi này bởi cb_pd_tw_01. Vui lòng thử lại sau {n}s"** + tooltip + nút Thử lại. UI disable button + polling 5s auto-refresh state. | Negative 🟡 |
| TC-PD-025 | FR-II-08 / Mo_ta_cong_khai XSS sanitize F-38 | mo_ta_cong_khai paste `<script>` | cb_pd_tw_01 login. HD-M DA_DUYET. | mo_ta_cong_khai="Mô tả<script>alert(1)</script>" | 1. Modal Công khai. 2. Paste payload. 3. Submit. | (2) Sanitize 3-layer (client DOMPurify + server save + server pre-API). PHAN_HOI/HOI_DAP.mo_ta_cong_khai sạch. Counter chỉ đếm plain text (không tính HTML). | Negative 🟡 |
| TC-PD-026 | FR-II-08 / mo_ta boundary 2000 ký plain | mo_ta exact 2000 ký plain (boundary inclusive) | cb_pd_tw_01 login. HD-L DA_DUYET. | mo_ta=2000 ký | 1. Paste 2000 ký. 2. Counter "2000/2000 ký tự văn bản". 3. Submit. | (3) OK. | Edge 🟢 |
| TC-PD-027 | FR-II-08 / Permission Công khai BR-AUTH-05 + F-20 | CB_NV attempt Công khai | cb_nv_tw_01 login. HD-K DA_DUYET. | — | 1. Mở SCR-II-02. | (2) Nút [Công khai] KHÔNG hiển thị (chỉ CB_PD cùng cấp + đơn vị, F-20 + BR-AUTH-05). | Negative 🟡 |

---

## E. ĐÓNG HỒ SƠ — HAPPY + NEGATIVE (BR-FLOW-06)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-030 | FR-II-08 / SCR-II-02 dòng 18 + BR-FLOW-06 + AC #7 | CB NV cùng đơn vị đóng hồ sơ DA_DUYET → HOAN_THANH | cb_nv_tw_01 login. HD-J state DA_DUYET scope TW. | — | 1. SCR-II-02 HD-J. 2. Click [Đóng hồ sơ] dòng 18. 3. C12 "Đóng hồ sơ? Hồ sơ sẽ không thể chỉnh sửa." 4. Confirm. | (1) PUT thành công. (3) HD: `trang_thai=HOAN_THANH`, `ngay_hoan_thanh=NOW()`. (4) Audit log action='DONG_HO_SO'. | Happy 🔴 |
| TC-PD-031 | FR-II-08 / dòng 18 + BR-FLOW-06 CB PD path | CB PD cùng cấp đóng hồ sơ CONG_KHAI → HOAN_THANH | cb_pd_dp_01 login. HD-I state CONG_KHAI scope ĐP. | — | 1. Click [Đóng hồ sơ]. 2. Confirm. | (3) `trang_thai=HOAN_THANH`. | Happy 🟡 |
| TC-PD-032 | FR-II-08 / AC #8 BR-FLOW-06 KHÔNG auto-close | Bản ghi DA_DUYET 6 tháng không click "Đóng hồ sơ" → vẫn DA_DUYET | qtht_01 login. HD-H state DA_DUYET ngay_duyet=2025-11-01 (6 tháng trước). | — | 1. Verify state hôm nay. | (3) Vẫn DA_DUYET (KHÔNG auto-close per BR-FLOW-06 BA chốt 2026-05-05). Verify bằng cách check scheduled job list KHÔNG có job auto-close cho HOI_DAP. | Edge 🟡 |
| TC-PD-033 | FR-II-08 / dòng 18 permission cross-cấp | CB PD khác cấp attempt đóng hồ sơ | cb_pd_tw_01 login. HD-G state DA_DUYET scope ĐP. | — | 1. Mở SCR-II-02. | (2) Nút [Đóng hồ sơ] KHÔNG hiển thị (CB_PD cấp khác). | Negative 🟡 |

---

## F. PHÊ DUYỆT HÀNG LOẠT (BR-FLOW-02 + BR-EC-19)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-040 | FR-II-08 / AC #5 + BR-FLOW-02 | Phê duyệt batch 5 records OK | cb_pd_tw_01 login. ≥5 HD CHO_PHE_DUYET scope TW. | — | 1. Tab "Chờ phê duyệt". 2. Tick 5 checkboxes (dòng 19). 3. Action-bar dòng 34 "Đã chọn 5 bản ghi" + [Phê duyệt hàng loạt]. 4. Confirm. | (1) PUT batch per-record. (2) Modal "Duyệt thành công 5, lỗi 0". (3) 5 records đổi state DA_DUYET. Notification in-app cho 5 CB NV. Audit log 5 entries. | Happy 🔴 |
| TC-PD-041 | FR-II-08 / E8 ERR-PD-05 + BR-EC-19 | Batch >100 records | cb_pd_tw_01 login. ≥101 HD CHO_PHE_DUYET. | — | 1. Tick 101 records (force qua "Chọn tất cả" + scroll). 2. Click [Phê duyệt hàng loạt]. | (2) Toast: **"Mỗi lần phê duyệt tối đa 100 bản ghi. Vui lòng chọn ít hơn."** (ERR-PD-05). Block submit. | Negative 🔴 |
| TC-PD-042 | FR-II-08 / WRN-PD-01 + EC-03 | Batch partial fail (mix lỗi) | cb_pd_tw_01 login. Tick 5 records: 3 cùng cấp TW (OK) + 2 ĐP (khác cấp). | — | 1. Submit batch. | (2) Modal report: **"Duyệt thành công 3, lỗi 2"** (WRN-PD-01). Per-record detail: ERR-PD-01 cho 2 records ĐP. | Negative 🟡 |
| TC-PD-043 | FR-II-08 / ERR-BATCH-CONFLICT batch | Concurrent edit version mismatch trong batch | cb_pd_tw_01 tick 5 records. cb_pd_tw_02 sửa 1 record giữa chừng (UPDATE version). | — | 1. cb_pd_tw_01 submit batch. | (2) Report: "Thành công 4, skip 1: ERR-BATCH-CONFLICT — Bản ghi #{ma} đã được cb_pd_tw_02 cập nhật lúc {time}, đã skip. Tải lại + thử lại". | Negative 🟡 |

---

## G. CÔNG KHAI HÀNG LOẠT (action-bar dòng 35)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-050 | FR-II-08 / SCR-II-01 dòng 35 batch CK | Công khai batch 3 records DA_DUYET cùng cấp | cb_pd_tw_01 login. ≥3 HD DA_DUYET cùng cấp TW. Mock API Cổng OK. | — | 1. Tab "Đã duyệt". 2. Tick 3. 3. [Công khai hàng loạt]. | (2) Per-record API call. Modal report: "Đã công khai 3 bản ghi thành công, 0 lỗi". 3 records → CONG_KHAI. | Happy 🔴 |
| TC-PD-051 | FR-II-08 / dòng 35 cấp lẫn lộn | Tick records nhiều cấp khác nhau | cb_pd_tw_01 login. Tick 3 record TW (OK) + 2 record ĐP (khác cấp). | — | 1. Submit batch. | (2) Filter per-record: 3 TW pass, 2 ĐP skip. Modal report nhãn tiếng Việt: "Cổng Pháp luật Quốc gia không phản hồi" / **"Khác cấp đơn vị"** / "Cán bộ khác đã sửa giữa chừng" / "Đang khóa bản ghi". | Negative 🟡 |
| TC-PD-052 | FR-II-08 / dòng 35 API fail mix | Batch CK với 1 record API fail | cb_pd_tw_01 login. 3 records DA_DUYET. Mock API: 2 OK + 1 fail (timeout). | — | 1. Submit batch. | (2) Report: "Đã công khai 2 thành công, 1 lỗi: 'Cổng Pháp luật Quốc gia không phản hồi'" (ERR-PD-04 nội bộ). | Negative 🟡 |

---

## H. FR-II-09 ĐÃ XỬ LÝ (read-only) + EDGE

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-060 | FR-II-09 / AC #1 + AC #2 | Tab Hoàn thành hiển thị danh sách read-only + chi tiết timeline | cb_nv_tw_01 login. ≥5 HD HOAN_THANH scope TW. | — | 1. Tab "Hoàn thành". 2. Click 1 record → SCR-II-02. | (2) Bảng read-only (BR-FLOW-03). Chi tiết hiển thị toàn bộ lịch sử AUDIT_LOG dòng 27 + danh sách phản hồi cũ dòng 28 (nếu có). | Happy 🟡 |
| TC-PD-061 | FR-II-09 / E1 INF-DAXL-01 | Empty state khi chưa có HD hoàn thành | cb_nv_dp_01 (Sở TP X mới setup) login. 0 HD HOAN_THANH. | — | 1. Tab Hoàn thành. | (3) Empty: **"Chưa có hỏi đáp nào đã xử lý"** (INF-DAXL-01). | Edge 🟢 |
| TC-PD-062 | FR-II-09 / E3 ERR-DAXL-01 | Mở chi tiết record không tồn tại | cb_nv_tw_01 login. | URL `/hoi-dap/INVALID-ID` | 1. Paste URL. | (2) UI dòng 30: ERR-DAXL-01 "Hỏi đáp không tồn tại hoặc đã bị xóa" + nút Về danh sách. | Edge 🟡 |
| TC-PD-063 | FR-II-08 / EC-01 auto-escalate | CHO_PHE_DUYET >3 ngày LV không xử lý → escalate cấp trên | qtht_01 login. HD-Z CHO_PHE_DUYET, ngay_chuyen_pd=2026-05-01 (≥3 ngày LV trước). | — | 1. Trigger scheduled job (manual hoặc wait cron). 2. Verify notification. | (3) Notification in-app + email cho CB PD cấp trên (TW nếu BN, BN nếu ĐP — BR-AUTH-02). Audit log entry "Escalate". | Edge 🟡 |
| TC-PD-064 | FR-II-08 / SM-HOIDAP transition CONG_KHAI ↔ DA_DUYET cycle | Cycle Công khai → Hủy CK → Công khai lại OK | cb_pd_tw_01 login. HD-Y DA_DUYET. Mock API OK. | — | 1. Công khai → CONG_KHAI. 2. Hủy CK → DA_DUYET. 3. Công khai lại → CONG_KHAI. | (3) State cycle works. Audit log 3 entries. | Edge 🟡 |
| TC-PD-065 | FR-II-08 / Idempotency key | Re-submit Công khai khi network drop → idempotency chống duplicate | cb_pd_tw_01 login. HD-X DA_DUYET. Mock: API ack nhưng response timeout. User retry. | — | 1. Click [Công khai]. 2. Network timeout client. 3. Re-submit. | (3) Backend dùng idempotency key → KHÔNG tạo duplicate trên Cổng PLQG. State chuyển CONG_KHAI 1 lần. | Edge 🔴 |
| TC-PD-066 | FR-II-08 / Banner HUY state F-24 | Bản ghi HUY hiển thị banner thay stepper | cb_nv_tw_01 login. HD-W state HUY. | — | 1. Mở SCR-II-02. | (3) Stepper bình thường ẨN. Banner full-width "🚫 Đã hủy" + thông tin (thoi_gian_huy, nguoi_huy ho_ten + đơn vị, ly_do_huy). Action-bar 9-18 ẨN HẾT (read-only view). Lịch sử dòng 27 vẫn đầy đủ. | Edge 🟡 |
| TC-PD-067 | FR-II-08 / EC-02 batch optimistic locking edge | Batch >100 với optimistic locking concurrent | cb_pd_tw_01 batch 50 records. cb_pd_tw_02 batch overlap 30 records cùng pool. | — | 1. cb_pd_tw_01 submit. 2. cb_pd_tw_02 submit. | (3) Per-record lock + version check. cb_pd_tw_02 nhận ERR-BATCH-CONFLICT cho 30 records overlap. Report per-record. | Edge 🟡 |

---

---

## I. EDGE BỔ SUNG (A4 + A6 merged 2026-05-10)

| ID | TraceID | Tên Test Case | Pre-conditions | Test Data | Các bước thực hiện | Kết quả mong đợi | Type |
|----|---------|--------------|----------------|-----------|-------------------|------------------|------|
| TC-PD-068 | FR-II-08 / SPEC-CLARIFY-PD-08 | CB PD review HD có draft chưa gửi (ngay_tra_loi NULL) | cb_pd_tw_01 login. HD-Y CHO_PHE_DUYET. PHAN_HOI có draft với ngay_tra_loi IS NOT NULL (đã gửi) + 1 draft mới ngay_tra_loi NULL. | — | 1. Mở SCR-II-02 HD-Y. 2. Verify nội dung phản hồi hiển thị. | (3) **SPEC-CLARIFY-PD-08**: Hiển thị PHAN_HOI mới nhất có ngay_tra_loi NOT NULL (đã gửi). Draft NULL KHÔNG hiển thị cho CB PD. Verify thực tế. | Edge 🟢 |
| TC-PD-069 | FR-II-08 / Idempotency cycle | Hủy CK xong phê duyệt lại = đẩy lên Cổng PLQG (idempotency on update) | cb_pd_tw_01 login. HD-X cycle: CONG_KHAI → DA_DUYET (hủy CK) → CONG_KHAI (publish lại). Mock API tracking. | — | 1. Cycle 3 transitions trên cùng record. | (3) Mỗi lần Công khai: idempotency key MỚI (vì là PUBLISH mới chứ không phải retry). API Cổng PLQG nhận idempotency key khác → tạo entry mới hoặc update existing tùy contract. | Edge 🟡 |
| TC-PD-070 | FR-II-08 / BR-FLOW-03 undo prevent | Đóng hồ sơ rồi không undo được | cb_nv_tw_01 login. HD-W vừa đóng (HOAN_THANH). | — | 1. SCR-II-02 HD-W. | (3) Mọi action button (9-18) ẨN/disabled. State HOAN_THANH read-only (BR-FLOW-03). KHÔNG có nút "Mở lại hồ sơ". | Edge 🟡 |
| TC-PD-071 | FR-II-08 / Batch CK filter pre-submit | Batch CK records mix DA_DUYET + state khác (auto-skip) | cb_pd_tw_01 login. Tab "Đã duyệt" + force tick records từ tabs khác (DOM manipulation). | — | 1. Force tick 3 DA_DUYET + 2 CHO_PHE_DUYET. 2. [Công khai hàng loạt]. | (2) UI filter pre-submit: chỉ submit DA_DUYET records. Hoặc backend reject: "2 records không ở state DA_DUYET, đã skip". | Edge 🟡 |
| TC-PD-072 | FR-II-08 / Inputs anh_dai_dien boundary | Modal Công khai upload ảnh > 5MB → reject | cb_pd_tw_01 login. HD-V DA_DUYET. | anh_dai_dien=ảnh 5.5MB | 1. Click [Công khai]. 2. Upload ảnh 5.5MB. | (2) Reject inline: "Ảnh đại diện tối đa 5MB". File không upload. | Edge 🟢 |
| TC-PD-073 | FR-II-09 / ERR-AUTH-DAXL-01 (GAP-A5-06 fix) | Cross-tenant attempt xem HD đã xử lý | cb_nv_dp_02 (Sở TP BG) login. HD-AG state HOAN_THANH thuộc Sở TP AG. | URL `/hoi-dap/HD-AG-id` | 1. cb_nv_dp_02 paste URL. | (2) HTTP 403 với ERR-AUTH-DAXL-01: **"Bạn không có quyền xem dữ liệu đơn vị này"**. UI: redirect về SCR-II-01 hoặc error block dòng 31 "Bạn không có quyền xem hỏi đáp này". | Negative 🟡 |
| TC-PD-074 | FR-II-08 / F-42 line 1558 lock TTL expiry (Codex P0 G-01) | Lock TTL 30s expiry path — sau timeout API tự release lock + retry OK | cb_pd_tw_01 login. HD-Z DA_DUYET. Mock API Cổng PLQG: hang >30s không response. | — | 1. Click [Công khai] → submit. 2. Lock acquired, `api_in_progress=true`. 3. Wait >30s API không response. 4. TTL expire tự động release lock + clear flag. 5. cb_pd_tw_02 click [Công khai] cùng record. | (3) Sau 30s, lock tự release (KHÔNG cần API response). cb_pd_tw_02 acquire lock thành công. (4) Submit OK. KHÔNG nhận ERR-PD-07. Ref SRS line 1558 "Release lock khi API response (thành công/thất bại) hoặc khi TTL hết". (5) Audit log entry "lock_expired_ttl=30s". | Edge 🔴 (P0 G-01 fix) |
| TC-PD-075 | FR-II-08 / F-38 layer 3 sanitize line 1142 (Codex P0 G-02) | Layer 3 XSS sanitize pre-API outbound cho PHAN_HOI.noi_dung | cb_pd_tw_01 login. HD-Y DA_DUYET. PHAN_HOI.noi_dung đã stored DB chứa mixed HTML: `<p>Allowed</p><script>blocked</script><a href="javascript:alert(1)">link</a>` (giả lập case data drift hoặc bypass server save). | — | 1. Click [Công khai]. 2. Submit. 3. Inspect outbound API request payload qua list_network_requests MCP. | (3) Layer 3 sanitize trước khi đẩy lên Cổng PLQG: payload chứa CHỈ `<p>Allowed</p>` + `<a href="">link</a>` (strip `<script>` + `javascript:`). Verify SRS line 1142 "sanitize lần thứ 3 trước khi đẩy lên API Cổng Pháp luật Quốc gia (OWASP Java HTML Sanitizer / Python Bleach)". | Negative 🔴 (P0 G-02 fix) |
| TC-PD-076 | FR-II-08 / BR-AUTH-05 same-cap cross-unit (Codex P2 I-01) | CB_PD_BN từ Bộ A approve record của Bộ B (cùng cap=BN) → PASS | cb_pd_bn_01 (Bộ KH&ĐT) login. HD-X CHO_PHE_DUYET thuộc Bộ Tài chính (cùng cap=BN). | — | 1. cb_pd_bn_01 mở SCR-II-02 HD-X. 2. Click [Phê duyệt]. | (2) PASS — BR-AUTH-05 chỉ check `cap` (TW=TW, BN=BN, DP=DP), KHÔNG check `don_vi_id`. Per SRS line 1164 "user.role = CB_PD_{cap} AND user.don_vi.cap = record.don_vi.cap". HD chuyển DA_DUYET. (Đối chiếu với TC-PD-100 negative cross-cấp đã có.) | Happy 🟡 (P2 I-01 fix) |

---

## Tổng kết file 07

- **Tổng số TC: 38** (Phê duyệt 2H + Từ chối 1H+3N + 3N permission + Công khai 1H+5N + Đóng hồ sơ 2H+2 edge + Batch PD 1H+3N + Batch CK 1H+2N + FR-II-09 1H+2 edge + 5 edge cross-cutting + 6 A4/A6 merged)
- **Critical TC (🔴)**: TC-PD-001, 010, 020, 022, 030, 040, 100, 011, 021, 050, 041, 065
- **Coverage**: FR-II-08 đầy đủ (Phê duyệt + Từ chối + Công khai + Hủy CK + Đóng hồ sơ + 2 batch types) + FR-II-09 read-only + BR-AUTH-05 + BR-FLOW-02/04/05/06 + BR-EC-19/20 + EC-01..05 + F-20/F-42/F-24
- **Error codes**: ERR-PD-01..07, WRN-PD-01, INF-DAXL-01, ERR-DAXL-01 (đầy đủ 8 codes)
- **F-references**: F-08 (modal Công khai), F-07 (modal Từ chối), F-20 (Công khai cùng cấp + đơn vị), F-42 (lock TTL 30s outbound), F-24 (banner HUY), F-38 (XSS mo_ta)
- **API outbound mock**: cần infra mock Cổng PLQG cho test isolation

*Generated 2026-05-10 — Phase A step A3*
