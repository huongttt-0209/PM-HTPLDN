# BA confirmation needed — Lô B7 · Mạng lưới Tư vấn viên — 2026-08-06

> **⚠️ File này là bản ghi gốc của lô, KHÔNG phải bản gửi BA.**
> Bản gửi BA là [`cau-hoi-BA-tong-hop-2026-08-06.md`](../reverify-week-5/ba-confirm/cau-hoi-BA-tong-hop-2026-08-06.md) — `QLTVV_02` → **Mục 14**.

> Gom điểm QA **không tự chốt được** vì đặc tả im lặng. Bug có căn cứ đặc tả rõ đã ghi ở
> [`bug-report.md`](bug-report.md) — không lặp ở đây.
>
> **Môi trường + bản dựng đã đo:** `https://18.143.165.120.nip.io` (env nội bộ) · `HTPLDN · V1.0.8` ·
> bó mã FE `assets/index-DIABnbIr.js` · `GET /` `last-modified 06/08/2026 14:13:15` giờ VN.
>
> **Nguồn quote số dòng:** `Docs-PM-HTPLDN/_bmad-output/planning-artifacts/srs-v3.5/`.

---

## QLTVV_02 — Danh sách Tư vấn viên / Chuyên gia mặc định sắp xếp theo tiêu chí nào?

**Bối cảnh**

- Dòng Excel: **32**, tab `bug`, mã TC `QLTVV_02` — *"Kiểm tra hiển thị bảng danh sách"*.
- Màn: **Mạng lưới Tư vấn viên → Tư vấn viên / Chuyên gia** (`SCR-IV-01`), tab mặc định *"Đang hoạt động"*.
- Case gộp **5 vế**. **4 vế đã hết lỗi** sau lượt đo 06/08 (không tràn/đè · hiển thị điểm đã đồng nhất ·
  nút thao tác không xuống dòng · mặc định 20 mục/trang). Mục hỏi BA này là **vế thứ 5**, và nó chính là
  thứ đang giữ verdict của case ở mức **cần BA** thay vì Pass.

**Đối tác kỳ vọng gì**

- Ô *"Kết quả mong đợi"* của phiếu ghi nguyên văn: *"Mặc định: hệ thống **sắp xếp theo ngày công nhận mới
  nhất trước**, 20 bản ghi mỗi trang"*.
- Ô *"Kết quả thực tế"* (vòng 1, 07/07) ghi: *"Hệ thống không mặc định sắp xếp theo ngày công nhận mới nhất"*.

**Phần mềm đang làm gì (đo 06/08/2026)**

- Tài khoản `cbnv_tw_02` — vai trò **CB_NV_TW**, cấp **TW** (trùng khít vai trò + cấp trên ảnh của đối tác).
- Đọc cột **"Ngày công nhận" của toàn bộ 6/6 hàng** trang 1 (không dừng ở vài hàng đầu), thứ tự hiển thị:
  `—` · `17/07/2026` · `12/07/2026` · `—` · `—` · `—` ⇒ **không giảm dần**, và hàng trống cũng không dồn
  về một phía.
- Đối chiếu bằng đường thứ hai — đọc lại chính lời gọi danh sách mà giao diện dùng: thứ tự máy chủ trả về
  **trùng khít** thứ tự trên màn (nên không phải giao diện xáo), và trường **ngày tạo** của dãy đó **giảm
  dần tuyệt đối**: `05/08/2026` → `12/07/2026 09:55` → `12/07/2026 00:11` → `30/06/2026` → `01/03/2026` →
  `01/02/2024`.
- ⇒ Danh sách đang sắp theo **ngày tạo bản ghi, mới nhất trước** — một tiêu chí khác với ngày công nhận.
- Bằng chứng: `image/QLTVV_02-03-1920-toan-bang-cot-NgayCongNhan-khong-giam-dan.png` (toàn bảng, đọc được
  cả cột Ngày công nhận lẫn chân bảng) · `image/QLTVV_02-01-1440-cuon-phai-DiemDG-TrangThai-Ngay-HanhDong.png` ·
  số đo đầy đủ ở `ketqua-QLTVV_02.txt` mục D · phản hồi máy chủ nguyên bản ở `tvv-list.network-response`.

**Điểm đặc tả im lặng**

- Đã tra **toàn bộ** `srs-fr-04-chuyen-gia-tvv.md` bằng `sắp xếp` / `sort` / `ORDER BY` / `DESC` /
  `mới nhất trước` → **0 kết quả**.
- `srs-fr-04-chuyen-gia-tvv.md:243`-`:247` (FR-IV-02 §Processing) chỉ có: kiểm quyền → kết hợp điều kiện
  AND → **phân trang (mặc định 20/trang)**. **Không có bước sắp xếp.**
- `srs-fr-04-chuyen-gia-tvv.md:1440`-`:1457` (bảng thành phần `SCR-IV-01`, liệt kê đóng 29 thành phần) mô tả
  từng cột và phần phân trang, **không nói cột nào là cột sắp xếp mặc định**.
- `BR-DATA-07` (`srs-fr-05-vu-viec.md:2392`-`:2394`) chỉ quy định *"Mọi danh sách sử dụng phân trang.
  Default: 20 rows/page, max: 100 rows/page"* — **không nói thứ tự**.
- Đối chiếu cho thấy đây là chỗ **bỏ trống riêng của nhóm IV**, không phải nằm ở tài liệu khác: các nhóm
  khác **có** quy định thứ tự — `srs-fr-08-danh-gia.md:904`, `srs-fr-12-tv-chuyen-sau.md:1132`,
  `srs-fr-05-vu-viec.md:1665`.
- ⇒ Không có căn cứ đặc tả để chấm phần mềm đúng hay sai ở vế này.

**Câu hỏi cần BA xác nhận**

Danh sách `SCR-IV-01` khi mở lần đầu (chưa đụng bộ lọc, chưa bấm tiêu đề cột) phải sắp theo tiêu chí nào?

1. **Hướng 1 — ngày công nhận mới nhất trước** (đúng kỳ vọng đối tác ghi trong phiếu): phải bổ sung quy định
   vào `FR-IV-02 §Processing` **và** nói rõ **bản ghi chưa có ngày công nhận thì xếp ở đâu** — trên màn hiện
   có 4/6 bản ghi bỏ trống cột này, nên nếu không chốt chỗ đứng của nhóm trống thì vòng UAT sau vẫn tranh cãi.
2. **Hướng 2 — ngày tạo mới nhất trước** (đúng hiện trạng): xin xác nhận để QA ghi thành **quy ước đã chốt**
   và bổ sung một dòng vào đặc tả, các vòng UAT sau không mở lại phiếu ở điểm này.
3. **Hướng 3 — tiêu chí khác** (vd theo mã tư vấn viên, theo tên): BA chốt giúp tiêu chí và chiều sắp xếp.

**Đề xuất QA tạm thời**

- **Không** log thành lỗi: đặc tả im lặng, không có dòng nào để đối chiếu đúng/sai. Verdict case `QLTVV_02`
  để ở **cần BA** (4 vế còn lại đã hết lỗi, không vế nào đang lỗi).
- Nếu BA chọn **hướng 1** → mở 1 phiếu mức **Minor**, owner `Dev BE` (thêm mệnh đề sắp xếp vào truy vấn
  danh sách) + `BA` bổ sung dòng đặc tả kèm quy tắc cho bản ghi trống ngày công nhận.
- Nếu BA chọn **hướng 2** → owner `BA`, chỉ bổ sung một dòng vào `FR-IV-02 §Processing`; không đụng phần mềm.
