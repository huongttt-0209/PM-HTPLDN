# Evidence audit — QLDMTCTV_02 (verdict `Pass`)

**Mã TC:** QLDMTCTV_02 · **Dòng sheet:** 317 · **Tab:** `UAT_TGPL Doanh Nghiệp-tuần 3`
**Ngày verify:** 2026-08-03 · **Người verify:** QA Automation (Chrome DevTools MCP)
**Môi trường QA:** https://18.143.165.120.nip.io — bản dựng hiển thị ở chân menu: `HTPLDN · V1.0.5`
**Cột P (`Trạng thái dev fix 1`):** `dev done` — giữ nguyên, KHÔNG đụng. **Verdict ghi ở cột Q (Verify): `Pass`.**

## Note dev trước khi QA đè

(cột R rỗng tại 2026-08-03 — dev không để lại note)

---

## 1. Bằng chứng đối tác đã xem

| Mục | Nội dung |
|---|---|
| File | `partner-evidence/QLDMTCTV_02.jpg` — ảnh tĩnh, đã mở FULL-RES bằng tool Read (không đọc qua mô tả text) |
| Khoảnh khắc lỗi | Chính khung hình: hàng tiêu đề bảng bắt đầu bằng `Mã tổ chức` — **không có ô tích chọn, không có cột STT** |
| Vai trò trong ảnh | "Quản trị viên · QTHT", phạm vi `BTP · TW` |
| Trạng thái đang đứng | Thẻ "Đang hoạt động" được chọn; thanh thẻ có 6 mục (có cả "Chờ phê duyệt") |
| Dữ liệu tiền đề | Bảng có ≥5 tổ chức: `TC-STP-HN-0001`, `TC-BTP-TW-0008/0007/0005/0004` |
| Thời điểm | Đồng hồ máy đối tác: 2026-07-28 08:54 |

**Kết luận Cổng 1 + 2:** đối tác quan sát ĐÚNG trên bản dựng ngày 28/07 — thiếu thật 2 thành phần.

## 2. SRS đối chiếu (dẫn dòng, đã mở file đọc trực tiếp)

Nguồn duy nhất: `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/srs-fr-04-chuyen-gia-tvv.md`

| Dòng | Trích |
|---|---|
| 1027 | `### FR-IV-NEW-01: Quản lý Tổ chức tư vấn` |
| 1029 | `**UC Reference:** (chưa có trong CSV — gắn [GAP-IV-07])` → **FR này không có mã UC trong SRS** |
| 1608 | `### SCR-IV-NEW-01: Danh sách Tổ chức tư vấn` |
| 1612 | `**Đường dẫn:** /chuyen-gia-tvv/to-chuc` |
| 1637 | hàng 15 — `bảng \| Ô chọn \| checkbox \| Chọn nhiều dòng cho thao tác hàng loạt` |
| 1638 | hàng 16 — `bảng \| Số thứ tự \| cột \| Tự động đánh số theo trang` |
| 1639–1646 | các cột: Mã tổ chức · Tên tổ chức · Loại hình · Người đại diện · Lĩnh vực · Trạng thái · Công khai · Hành động |
| 1647 | hàng 25 — thao tác hàng loạt `Công khai` / `Hủy công khai` (thẻ "Đang hoạt động"), hiện khi chọn ≥1 dòng |
| 1648 | hàng 26 — thao tác hàng loạt `Phê duyệt hàng loạt` (thẻ "Chờ phê duyệt"), vai trò Cán bộ Phê duyệt cùng đơn vị |
| 1628 | hàng 6 — thẻ "Chờ phê duyệt": *"Hiển thị khi vai trò là Cán bộ Phê duyệt"* |

## 3. Quan sát trên web (artifact real-data — loại claim "Hiển thị/render")

**Phương pháp 1 — đọc thô cây DOM** (`innerText` từng `<th>`, **không** dùng `textContent`; kèm `outerHTML` của `<thead>` để tự kiểm selector):

```
soTh = 11
th[0]  = ""                → <th class="ant-table-cell ant-table-selection-column">
                              chứa <input aria-label="Select all" type="checkbox">
th[1]  = "STT"
th[2]  = "Mã tổ chức"      th[3] = "Tên tổ chức"     th[4]  = "Loại hình"
th[5]  = "Lĩnh vực"        th[6] = "Đơn vị quản lý"  th[7]  = "Người đại diện"
th[8]  = "Trạng thái"      th[9] = "Công khai"       th[10] = "Hành động"

thead checkbox = 1 · mỗi tr.ant-table-row có đúng 1 checkbox · STT các dòng = 1, 2, 3
```

**Phương pháp 2 — ảnh full-res đã mở ra ĐỌC** (không chỉ lưu): nhìn thấy rõ ô tích ở hàng tiêu đề và ở từng dòng, cột STT với giá trị 1/2/3.

→ **2 phương pháp trùng khớp** (yêu cầu "bug candidate ≠ bug" của postmortem 16/07). Không có mâu thuẫn nào.

**Đã tải lại trang bỏ qua bộ nhớ đệm** (hard reload) rồi đo lại: kết quả y hệt → không phải do tab MCP mở lâu còn chạy mã cũ.

### Ảnh chụp web (đều đã mở ra đọc, tên file khớp nội dung pixel)

| Ảnh | Nội dung xác nhận |
|---|---|
| `image/QLDMTCTV_02-tab-dang-hoat-dong-co-o-chon-va-stt.png` | Thẻ "Đang hoạt động" (3 dòng), vai trò CB Nghiệp vụ TW — có ô tích + cột STT |
| `image/QLDMTCTV_02-chon-nhieu-dong-hien-thao-tac-hang-loat.png` | Chọn 3 dòng → thanh "Đã chọn 3 tổ chức tư vấn" + nút Công khai / Hủy công khai / Bỏ chọn (SRS dòng 1647) |
| `image/QLDMTCTV_02-vai-tro-quan-tri-vien-qtht-giong-doi-tac-co-o-chon-va-stt.png` | **Đúng vai trò của đối tác** (Quản trị viên · QTHT · BTP·TW) — cũng có ô tích + cột STT |
| `image/QLDMTCTV_02-tab-moi-dang-ky-co-o-chon-va-stt-khong-co-nut-phe-duyet-hang-loat.png` | Thẻ "Mới đăng ký" (1 dòng QA tự seed) — có ô tích + STT |
| `image/QLDMTCTV_02-tab-cho-phe-duyet-o-chon-stt-va-nut-phe-duyet-hang-loat.png` | Thẻ "Chờ phê duyệt" với vai trò CB Phê duyệt TW — ô tích + STT + nút **Phê duyệt hàng loạt** (SRS dòng 1648) |
| `image/QLDMTCTV_02-cuon-ngang-hien-cot-trang-thai-va-cong-khai.png` | Cuộn ngang bảng — thấy rõ cột Trạng thái (badge) và Công khai; không tràn/đè chữ |
| `image/QLDMTCTV_02-seed-form-them-moi-truoc-khi-luu.png` | Bước seed: biểu mẫu Thêm mới đã điền trước khi lưu |
| `image/QLDMTCTV_02-seed-sau-khi-luu-thong-bao.png` | Bước seed: sau khi lưu, thẻ "Mới đăng ký" hiện số đếm 1 |
| `image/QLDMTCTV_02-seed-trinh-phe-duyet-thong-bao.png` | Bước seed: sau khi Trình phê duyệt, trạng thái đổi thành "Chờ phê duyệt" |

## 4. Đóng GAP điều kiện (không đóng bằng lập luận)

- **Vai trò:** đối tác dùng Quản trị viên (QTHT). QA đã đăng nhập đúng vai trò đó trong một phiên trình duyệt cách ly để đối chứng, **nhưng verdict đặt trên tài khoản nghiệp vụ `cbnv_tw_04`** (đúng nguyên tắc "admin không dùng ra verdict"). Thêm `cbpd_tw_04` để mở được thẻ "Chờ phê duyệt".
- **Dữ liệu:** các thẻ ngoài "Đang hoạt động" đều rỗng → QA **tự tạo** tổ chức `TC-BTP-TW-0001` qua giao diện rồi **tự trình phê duyệt**, không lấy "thiếu dữ liệu" làm lý do bỏ qua.
- **Trạng thái:** đã đọc hàng tiêu đề ở cả 6 thẻ; 3 thẻ có dữ liệu thật (Đang hoạt động, Mới đăng ký, Chờ phê duyệt).

## 5. Kiểm soát chất lượng phép đo (postmortem 16/07)

- Bộ bắt thông báo: dùng đúng `tools/toast-capture.js`, **không lọc trùng**, đọc bằng `innerText`. Tự kiểm trước mỗi lần đo: `soObserverDangSong = 1` (hợp lệ) ở cả 2 lần.
- Đếm request song song với thông báo ở **mọi thao tác đổi trạng thái**:
  - Tạo tổ chức: `SO_REQUEST = 1` (`POST /api/v1/to-chuc-tu-vans`) · `SO_KHUNG_THONG_BAO = 1` ("Tạo Tổ chức tư vấn thành công") → không lặp.
  - Trình phê duyệt: `SO_REQUEST = 1` (`POST /api/v1/to-chuc-tu-vans/{id}/trinh-phe-duyet`) · `SO_KHUNG_THONG_BAO = 1` ("Đã trình phê duyệt") → không lặp.
- **Một phép đo của QA đã nói dối:** script báo bấm "Trình phê duyệt" ra `0 request / 0 thông báo / không có hộp thoại`. Kiểm lại bằng cây trợ năng thì hộp thoại "Xác nhận trình phê duyệt" VẪN mở bình thường → nguyên nhân là **selector `.ant-modal-content` của QA không khớp**, không phải lỗi ứng dụng. **Không log.** (Đúng dấu hiệu "selector không khớp → đừng kết luận chức năng hỏng" ở §4 postmortem.)

## 6. Lập luận verdict

1. Đối tác phản ánh **thiếu ô chọn và thiếu cột STT**. SRS quy định rõ 2 thành phần này (dòng 1637, 1638).
2. Trên bản dựng hiện tại, **cả 2 đều CÓ**, xác nhận bằng 2 phương pháp độc lập + ảnh full-res đã đọc, ở **cả vai trò của đối tác** lẫn vai trò nghiệp vụ, ở **mọi thẻ trạng thái**.
3. Ô chọn không chỉ hiển thị mà **dùng được thật**: kéo theo đúng 2 chức năng hàng loạt SRS mô tả (dòng 1647 và 1648).
4. 8 cột còn lại của SRS đều hiện đủ; không tràn/đè chữ; ngôn ngữ thống nhất.
5. Cột P đã là `dev done` và **kiểm chứng cho thấy claim của dev là ĐÚNG** → theo bảng verdict: **`Pass`**.

## 7. Lỗi phát hiện thêm ngoài phạm vi case (dựa trên ảnh đã đọc — chưa log, chờ user quyết)

| # | Quan sát | Đối chiếu SRS | Mức |
|:-:|---|---|---|
| 1 | Cột "Công khai" là **thẻ tĩnh** `<span class="ant-tag">`, nhãn "Công khai" / "Riêng tư", `cursor:auto`, bấm không mở hộp thoại nào | SRS dòng 1645 mô tả **toggle**, nhãn "Đã công khai"(xanh) / "Chưa công khai"(xám), *"Click → mở MD-CONG-KHAI hoặc MD-HUY-CONG-KHAI"* | Nhỏ — chức năng công khai vẫn làm được qua nút hàng loạt |
| 2 | Bảng có thêm cột **"Đơn vị quản lý"** | SRS liệt kê "Đơn vị quản lý" ở dòng 1634 như một **bộ lọc**, không nằm trong danh sách cột (1637–1646) | Nhỏ — thừa so với đặc tả, không thiếu thông tin |
| 3 | Cột "Hành động" dùng 3 icon rời, **không có dropdown "..."**; mục "Trình phê duyệt" nằm ở màn chi tiết | SRS dòng 1646 mô tả 2 icon + dropdown "..." chứa Trình phê duyệt / Phê duyệt / Từ chối / Cập nhật trạng thái / Xóa | Nhỏ — thao tác vẫn thực hiện được đầy đủ (đã tự chạy Trình phê duyệt thành công) |

> Cả 3 mục **nằm ngoài** phản ánh của đối tác ở case này và đều không chặn nghiệp vụ. Theo postmortem 16/07 mục C1/B2, chúng được ghi lại ở đây và báo về user để user quyết có mở dòng TC mới bằng `tools/sheet_add_bug_row.py` hay không — QA **không tự ghi** vào sheet đối tác.

## 8. Dữ liệu QA để lại trên môi trường

- `TC-BTP-TW-0001` — "Trung tam Tu van QA Kiem Cot Bang 0803", loại hình Công ty Luật, lĩnh vực Thương mại, đơn vị Cục Bổ trợ tư pháp - Bộ Tư pháp. Hiện ở trạng thái **Chờ phê duyệt** (QA tạo bằng `cbnv_tw_04` rồi tự trình duyệt, **chưa** phê duyệt). Giữ lại làm dữ liệu tiền đề cho các case cần trạng thái này.
