# KTHSYCHTPL_03 — Bảng đối chiếu điều kiện

**Case:** Kiểm tra hiển thị Nhóm 1 — Thông tin Doanh nghiệp (SCR-V.I-03, Accordion 1).
**Evidence đối tác:** `partner-evidence/KTHSYCHTPL_03.webm` — frame 00m22s: nhóm "Thông tin Doanh nghiệp" mở ra, chỉ có 5 ô (Tên DN "—", Mã số thuế "—", Địa chỉ "—", Người tiếp nhận, Email "—").
**Đối tác phản ánh:** (a) không hiển thị thông tin DN dù có dữ liệu phù hợp; (b) thiếu các trường Tỉnh/Thành, Loại doanh nghiệp, Quy mô doanh nghiệp, Người đại diện, Số điện thoại.

| Điều kiện có thể đổi kết quả | Đối tác (từ evidence, full-res) | Mình test | GAP? |
|---|---|---|:-:|
| Vai trò / tài khoản | CB_NV_TW — header "Cán bộ NV Trung ương / CB_NV_TW" (frame 00m22s) | `cbnv_tw` — header "CB Nghiệp vụ - Trung ương / CB_NV_TW" | Không |
| Entity + trạng thái (state machine) | VV-BTP-TW-20260525-001 — trạng thái "Đang kiểm tra" | VV-BTP-TW-20260712-003 — trạng thái "Đang kiểm tra" (đã đi qua Kiểm tra hồ sơ, kết luận Đạt) | Không |
| Dữ liệu tiền đề (DN liên kết có dữ liệu trong DB) | VV có DN liên kết (đối tác khẳng định "tồn tại dữ liệu phù hợp") | VV liên kết DN-SEED-0001; đã **seed đủ dữ liệu** cho DN: Tên DN, MST 0100000001, Địa chỉ, Người đại diện, Điện thoại, Email, Quy mô, Ngành nghề, Loại DN, Tỉnh/Thành — lưu thành công, đọc lại sau reload vẫn còn | Không |

## Quan sát (real-data)

Nhóm "Thông tin Doanh nghiệp" trên web QA — **chỉ render 5 ô**, 4/5 ô giá trị "—" dù DN đã có đủ dữ liệu:

```json
{"stateNow":"Đang kiểm tra","cellCount":5,"hasLinkToDNDetail":false,
 "dnCells":[{"label":"Tên Doanh nghiệp","value":"—"},
            {"label":"Mã số thuế","value":"—"},
            {"label":"Địa chỉ","value":"—"},
            {"label":"Người tiếp nhận","value":"CB Nghiệp vụ - Trung ương"},
            {"label":"Email","value":"—"}]}
```

**Chứng minh dữ liệu CÓ tồn tại (loại trừ giả thuyết "DN rỗng"):**
- Màn Doanh nghiệp → DN-SEED-0001 sau khi lưu + reload: Tên "Công ty TNHH Seed Publishable", MST "0100000001", Địa chỉ "So 10 Pho Test, Quan Ba Dinh, Ha Noi", Người đại diện "Nguyen Van Seed", Điện thoại "0243777888", Email "seed.publishable@test.htpldn.vn".
- Danh sách Vụ việc HTPL: cột "Tên DN" của chính VV này hiển thị "Công ty TNHH Seed Publishable" → VV có liên kết DN.
- API chi tiết vụ việc (`GET /api/v1/vu-viecs/{id}`) trả `"doanhNghiepId":"5eed0010-0000-4000-8000-000000000001"` nhưng `"doanhNghiep": null` → dữ liệu DN không được trả kèm, nên màn chi tiết in "—".

Ảnh: `../../bug-reports/image/BUG-KTHSYCHTPL_03-web-nhom1-thongtin-dn-trong-va-thieu-truong.png`

## Đối chiếu SRS (Cổng 3)

- **SRS yêu cầu** — `srs-fr-05-vu-viec.md:1719` (SCR-V.I-03, Thành phần row 4 — Accordion 1 "Thông tin DN", read-only): các trường **ten_doanh_nghiep, ma_so_thue, dia_chi, tinh_thanh, loai_dn, quy_mo, nguoi_dai_dien, email, SDT** + **Link sang chi tiết DN (MH-07.2)**. Điều kiện hiển thị: **Luôn**.
- **Thực tế web** — chỉ có 4/9 trường SRS (Tên DN, MST, Địa chỉ, Email) và **tất cả đều in "—"**; thêm 1 trường KHÔNG có trong SRS ("Người tiếp nhận"); **không có link sang chi tiết DN**.
- **Kết luận** — THIẾU 5 trường (**Tỉnh/Thành, Loại DN, Quy mô, Người đại diện, Số điện thoại**) + THIẾU link chi tiết DN + 4 trường còn lại KHÔNG hiển thị dữ liệu dù DB có dữ liệu → **cả 2 ý của đối tác đều tái hiện**.
