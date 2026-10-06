# Phản hồi BA cho QA — UAT Tuần 1 (Nhóm II: Hỏi đáp pháp lý)

**Ngày lập:** 08/07/2026 · **Người lập:** BA
**Nguồn:** file UAT gốc `docs/Reference/Fix bug KTĐL/7. Trợ giúp pháp lý Doanh nghiệp - UAT_TGPL Doanh Nghiệp.csv`; SRS `_bmad-output/planning-artifacts/srs-v3.5/`
**Phạm vi:** 5 testcase — `QLCHVMDXL_01`, `QLTNXLHDVM_06`, `QLCHVMDXL_06`, `PHCHVM_01`, `PHCHVM_06`.

---

## Tóm tắt

| Testcase | Kết luận | Việc cần làm |
|----------|----------|--------------|
| `QLCHVMDXL_01` | Không phải bug | Đối tác sửa Expected |
| `QLTNXLHDVM_06`, `QLCHVMDXL_06` | (a) Lỗi thật: thiếu cột Người duyệt/Ngày duyệt · (b) Expected sai phần lọc trạng thái | (a) Dev bổ sung cột · (b) đối tác sửa Expected · sync SRS theo Hướng 2 |
| `PHCHVM_01` | (a) Lỗi thật: thiếu trường "Tệp đính kèm phản hồi" · (b) Expected sai phần giới hạn ký tự | (a) Dev bổ sung trường · (b) đối tác sửa Expected |
| `PHCHVM_06` | Không phải bug (giới hạn 20.000 là đúng) | Đối tác sửa Expected · sync SRS |

---

## `QLCHVMDXL_01` — tab "Đang xử lý"

**Kết luận:** Không phải bug. Testcase đăng nhập bằng CB_NV; phần mềm đúng SRS.

**Expected đối tác cần sửa:**
1. Bỏ trạng thái `DA_PHAN_CONG` (không tồn tại). Tab "Đang xử lý" chỉ lọc `TIEP_NHAN`, `DANG_XU_LY`. (SRS `srs-fr-02-hoi-dap.md:1020`)
2. Không đòi ẩn nút "Thêm mới". CB_NV có quyền tạo (`HOI_DAP_CREATE`) nên nút hiển thị ở mọi tab. (SRS `:1015`)
3. Không đòi ẩn nút "Xóa". Bản ghi `TIEP_NHAN`/`DANG_XU_LY` chưa ở trạng thái cuối nên có nút Xóa; chỉ khóa khi `DA_DUYET`/`CONG_KHAI`/`HOAN_THANH`. (SRS `:1044`)

---

## `QLTNXLHDVM_06` & `QLCHVMDXL_06` — tab "Hoàn thành"

**Actual (UAT gốc):** "Không có cột bổ sung Người duyệt, Ngày duyệt."

**(a) Thiếu cột "Người duyệt"/"Ngày duyệt" — LỖI THẬT, chuyển Dev.**
SRS bắt buộc 2 cột này (`srs-fr-02-hoi-dap.md:154`; FR-II-09/10 Output `:801-802`). Expected của đối tác ở điểm này đúng, giữ nguyên.

**(b) Bộ lọc trạng thái — Expected sai, đối tác sửa.**
BA chốt: tab "Hoàn thành" chỉ gồm `HOAN_THANH`, `HUY` (chỉ đọc). `DA_DUYET` và `CONG_KHAI` xem ở tab riêng.
→ **Expected sửa:** tab "Hoàn thành" = `trang_thai IN ('HOAN_THANH','HUY')`; chỉ đọc; có cột Người duyệt/Ngày duyệt; cột Hành động chỉ có "Xem".

**Đóng testcase** sau khi Dev bổ sung cột + đối tác chỉnh Expected phần lọc trạng thái.

---

## `PHCHVM_01` & `PHCHVM_06` — màn hình phản hồi

**Actual (UAT gốc):** `PHCHVM_01` = thiếu trường "Tệp đính kèm phản hồi" + hệ thống cho nhập 20.000 ký tự; `PHCHVM_06` = hệ thống cho nhập 20.000 ký tự.

**(a) `PHCHVM_01` thiếu trường "Tệp đính kèm phản hồi" — LỖI THẬT, chuyển Dev.**
SRS bắt buộc trường tải file đính kèm ở màn phản hồi (`srs-fr-02-hoi-dap.md:1124`). Expected ở điểm này đúng, giữ nguyên.

**(b) Giới hạn ký tự — không phải bug, đối tác sửa Expected.**
Ô **Nội dung phản hồi** = tối đa **20.000 ký tự** (`ERR-PH-03`) — đúng theo STT 7 UAT 26/05/2026 (nâng 5.000 → 20.000). Con số 5.000 là của ô **Nội dung câu hỏi** (`ERR-HD-02`), khác ô, không được nhầm.
→ **Expected sửa:** ô phản hồi cho nhập tối đa 20.000; nhập 20.001 mới báo `ERR-PH-03`. `PHCHVM_06` không phải bug.

---

## Tổng hợp việc cần làm

**Đối tác sửa Expected**
| Testcase | Sửa |
|----------|-----|
| `QLCHVMDXL_01` | Bỏ `DA_PHAN_CONG`; không đòi ẩn Thêm mới/Xóa với bản ghi chưa final |
| `QLTNXLHDVM_06`, `QLCHVMDXL_06` | Tab "Hoàn thành" = `HOAN_THANH, HUY`; giữ yêu cầu cột Người duyệt/Ngày duyệt |
| `PHCHVM_01`, `PHCHVM_06` | Giới hạn phản hồi = 20.000; giữ câu hỏi = 5.000; giữ yêu cầu trường "Tệp đính kèm phản hồi" |

**Dev sửa mã (2 lỗi thật, hiện dev fix InProcess — xác nhận build)**
| Testcase | Bổ sung |
|----------|---------|
| `QLTNXLHDVM_06`, `QLCHVMDXL_06` | Cột **Người duyệt / Ngày duyệt** ở tab "Hoàn thành" |
| `PHCHVM_01` | Trường **"Tệp đính kèm phản hồi"** ở màn soạn phản hồi |

**Sửa SRS — ĐÃ THỰC HIỆN 08/07/2026 ✅**
| File | Vị trí | Đã sửa |
|------|--------|--------|
| `srs-fr-02-hoi-dap.md` | FR-II-09 (mô tả + filter `:775`), FR-II-10 (`:831`) | Bộ lọc "đã xử lý" → `IN ('HOAN_THANH','HUY')` khớp tab Hoàn thành SCR-II-01 (Hướng 2) |
| `srs-v3.5.md` | `:2275` | `PHAN_HOI.noi_dung` 5.000 → 20.000 ký tự (khớp `srs-fr-02:1388`) |
