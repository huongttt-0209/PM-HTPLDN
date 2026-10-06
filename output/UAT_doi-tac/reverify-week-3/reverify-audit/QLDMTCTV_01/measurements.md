# Audit — QLDMTCTV_01 (row 141) — "Màn hình không có danh mục Tổ chức tư vấn"

**Verdict:** `Reject` (feature TỒN TẠI, chỉ chuyển vị trí menu theo CR-02)
**Ngày verify:** 2026-07-21 · **Account:** `admin` (QTHT) · **Tool:** Chrome DevTools MCP

## Cổng 1 — Evidence đối tác (ảnh full-res)
- File: `partner-evidence/QLDMTCTV_01.jpg` (chụp 2026-07-14, role QTHT).
- Env đối tác: `htpldn-uat.ospgroup.vn/quan-tri/danh-muc/CO_QUAN_DON_VI` (màn **Danh mục dùng chung**).
- Expected đối tác (sheet): "Quản lý danh sách các Tổ chức tư vấn tham gia mạng lưới."
- Actual đối tác (sheet): "Màn hình chức năng không có danh mục 'Tổ chức tư vấn'".
- → Đối tác kỳ vọng có mục "Tổ chức tư vấn" và không thấy nó **trong màn Danh mục dùng chung**.

## 3-Step Verify (đối chiếu SRS version)
1. **SRS version:** mở v3.5. Header dòng 7: *"...trừ **FR-VIII-06 đã chuyển sang FR-04**"*. Mục FR-VIII-06 (dòng 366-368): *"[ĐÃ CHUYỂN] Quản lý Tổ chức tư vấn đã chuyển sang Nhóm IV — xem FR-IV-NEW-01. [CR-02]"*.
2. **Quote SRS:**
   - `srs-v3.5/srs-fr-10-quan-tri.md:7` + `:366-368` — FR-VIII-06 đã chuyển đi.
   - `srs-v3.5/srs-fr-10-quan-tri.md:1569` — SCR-VIII-01 sidebar 15 tab, KHÔNG gồm "Tổ chức tư vấn".
   - `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1022` — FR-IV-NEW-01 "Quản lý Tổ chức tư vấn": CRUD tổ chức tư vấn tham gia mạng lưới.
   - `srs-v3.5/srs-fr-04-chuyen-gia-tvv.md:1327-1330` — menu: "Sub-menu: Tổ chức tư vấn → FR-IV-NEW-01/02/04" (SCR-IV-NEW-01 Danh sách / -02 Thêm-Sửa / -03 Chi tiết).
3. **Verify UI (method thực tế):**
   - Màn Danh mục dùng chung: DOM `body.innerText` KHÔNG chứa "Tổ chức tư vấn" (đúng như đối tác) → app đúng v3.5 (đã bỏ khỏi Danh mục).
   - Menu **Mạng lưới Tư vấn viên** có submenu **"Tổ chức tư vấn"** → click mở màn `/chuyen-gia-tvv/to-chuc` "Quản lý Tổ chức tư vấn".
   - Màn này FULL chức năng: 6 tab trạng thái (Đang hoạt động / Chờ phê duyệt / Mới đăng ký / Đã từ chối / Tạm dừng / Vô hiệu hóa), search + filter (Lĩnh vực / Đơn vị quản lý / Loại hình), Xuất Excel, 3 record (TC-STP-AG-0001, TCTV-SEED-0001, TC-TW-DEMO-001, "1-3 / 3 kết quả").

## Kết luận
- Feature "Quản lý danh sách Tổ chức tư vấn tham gia mạng lưới" (đúng expected đối tác) **TỒN TẠI và hoạt động** — nằm ở **Mạng lưới Tư vấn viên → Tổ chức tư vấn**, KHÔNG nằm ở Danh mục dùng chung.
- Theo SRS v3.5 (CR-02), FR-VIII-06 (Tổ chức tư vấn dạng danh mục QTHT) đã **chuyển** thành FR-IV-NEW-01 (chức năng nghiệp vụ Nhóm IV). App làm đúng v3.5.
- Đối tác chỉ tìm ở màn Danh mục dùng chung nên không thấy. Kỳ vọng của đối tác đã được đáp ứng ở vị trí mới → **`Reject`** (không phải bug; feature không mất).
- ⚠️ Session prompt giả định "thiếu tab → Open theo FR-VIII-06 dòng 366" là **dựa trên tiền đề cũ** — FR-VIII-06 đã bị deprecate/chuyển trong v3.5. Đã đính chính bằng 3-Step Verify version.

## Evidence ảnh
- `reverify-audit/QLDMTCTV_01/to-chuc-tu-van-group4.png` — màn "Quản lý Tổ chức tư vấn" ở Mạng lưới TVV (3 record, 6 tab trạng thái).
- `partner-evidence/QLDMTCTV_01.jpg` — màn Danh mục dùng chung đối tác chụp (không có tab Tổ chức tư vấn).
